from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import EmployeeForm

from core.models import Employee


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    query = request.GET.get("q", "")

    if query:
        employees = employees.filter(
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query)
        )

    return render(request, "core/employee_list.html", {
        "employees": employees,
        "query": query
    })


@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "core/employee_detail.html", {
        "employee": employee
    })


@login_required
def employee_create(request):
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("employee_list")

    return render(request, "core/employee_form.html", {
        "form": form,
        "title": "Добавить"
    })


@login_required
def employee_edit(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect("employee_detail", employee_id=employee.id)

    return render(request, "core/employee_form.html", {
        "form": form,
        "title": "Редактировать"
    })


@login_required
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return redirect("employee_list")
