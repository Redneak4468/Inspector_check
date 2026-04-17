import os
from pathlib import Path

from django.db.models import Q
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from docxtpl import DocxTemplate

from .forms import EmployeeForm
from .models import Employee, EmployeeAttachment


def _save_attachments(request, employee):
    for file_obj in request.FILES.getlist("attachments"):
        EmployeeAttachment.objects.create(
            employee=employee,
            file=file_obj,
            original_name=file_obj.name,
        )


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    query = request.GET.get("q", "")

    if query:
        employees = employees.filter(
            Q(last_name__icontains=query)
            | Q(first_name__icontains=query)
            | Q(middle_name__icontains=query)
        )

    return render(request, "core/employee_list.html", {"employees": employees, "query": query})


@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee.objects.prefetch_related("attachments"), id=employee_id)
    return render(request, "core/employee_detail.html", {"employee": employee})


@login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        employee = form.save()
        _save_attachments(request, employee)
        return redirect("employee_list")

    return render(request, "core/employee_form.html", {"form": form, "title": "Добавить"})


@login_required
def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    form = EmployeeForm(
        request.POST or None,
        request.FILES or None,
        instance=employee
    )

    if request.method == "POST" and form.is_valid():
        employee = form.save()

        for f in request.FILES.getlist("file"):
            EmployeeAttachment.objects.create(
                employee=employee,
                file=f,
                original_name=f.name
            )

        return redirect("employee_detail", employee_id=employee.id)

    return render(request, "core/employee_form.html", {
        "form": form,
        "employee": employee,
        "title": "Редактировать"
    })


@login_required
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return redirect("employee_list")


@login_required
def attachment_download(request, attachment_id):
    attachment = get_object_or_404(EmployeeAttachment, id=attachment_id)
    try:
        return FileResponse(
            attachment.file.open("rb"),
            as_attachment=True,
            filename=Path(attachment.original_name).name,
        )
    except FileNotFoundError as exc:
        raise Http404("Файл не найден") from exc


@login_required
def attachment_delete(request, attachment_id):
    attachment = get_object_or_404(EmployeeAttachment, id=attachment_id)
    employee_id = attachment.employee_id

    if request.method == "POST":
        attachment.delete()

    next_url = request.POST.get("next")
    if next_url:
        return redirect(next_url)

    return redirect(reverse("employee_edit", kwargs={"employee_id": employee_id}))


@login_required
def employee_export_docx(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    template_path = os.path.join(
        "templates_docs",
        "employee_template.docx"
    )

    doc = DocxTemplate(template_path)

    context = {
        "full_name": f"{employee.last_name} {employee.first_name} {employee.middle_name}",
        "position": employee.position,
        "department": str(employee.department) if employee.department else "",
        "inf_date": employee.inf_date.strftime("%d.%m.%Y") if employee.inf_date else "",
        "phone_number": employee.phone_number,
        "inf_name": employee.inf_name,
        "inf_source": employee.inf_source,
        "audit_subject": employee.audit_subject,
        "inf_text": employee.inf_text,
        "inf_result": employee.inf_result,
        "attachments": employee.attachments.all(),
    }

    doc.render(context)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    filename = f"employee_{employee.id}.docx"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    doc.save(response)

    return response
