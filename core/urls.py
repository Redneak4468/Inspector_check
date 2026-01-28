from django.urls import path
from .views import employee_list, employee_detail, employee_create, employee_edit, employee_delete

urlpatterns = [
    path('', employee_list, name="employee_list"),
    path("employee/<int:employee_id>/", employee_detail, name="employee_detail"),
    path("employee/add/", employee_create, name="employee_create"),
    path("employee/<int:employee_id>/edit/", employee_edit, name="employee_edit"),
    path("employee/<int:employee_id>/delete/", employee_delete, name="employee_delete"),
]
