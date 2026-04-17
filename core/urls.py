from django.urls import path

from .views import (
    attachment_delete,
    attachment_download,
    employee_create,
    employee_delete,
    employee_detail,
    employee_edit,
    employee_list,
    employee_export_docx,
)

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("employee/<int:employee_id>/", employee_detail, name="employee_detail"),
    path("employee/add/", employee_create, name="employee_create"),
    path("employee/<int:employee_id>/edit/", employee_edit, name="employee_edit"),
    path("employee/<int:employee_id>/delete/", employee_delete, name="employee_delete"),
    path("attachment/<int:attachment_id>/download/", attachment_download, name="attachment_download"),
    path("attachment/<int:attachment_id>/delete/", attachment_delete, name="attachment_delete"),
    path("employee/<int:employee_id>/export/", employee_export_docx, name="employee_export_docx"),
]
