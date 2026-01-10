from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from core.models import Employee


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "core/employee_list.html", {
        "employees": employees
    })


@login_required
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, "core/employee_detail.html", {
        "employee": employee
    })
