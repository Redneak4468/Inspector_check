from django.contrib import admin
from .models import Employee, Position, Department


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "position", "department", "inf_date")
    list_filter = ("position", "department", "inf_date")
    search_fields = ("last_name", "first_name", "middle_name", "inf_name")
    fieldsets = (
        ("Сотрудник", {
            "fields": (
                "last_name",
                "first_name",
                "middle_name",
                "position",
                "department",
                "phone_number",
            )
        }),
        ("Информация", {
            "fields": (
                "inf_name",
                "inf_date",
                "inf_source",
                "audit_subject",
                "inf_text",
                "inf_result",
            )
        }),
    )