from django.contrib import admin

from .models import Department, Employee, EmployeeAttachment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)


class EmployeeAttachmentInline(admin.TabularInline):
    model = EmployeeAttachment
    extra = 0
    fields = ("original_name", "file", "created_at")
    readonly_fields = ("created_at",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "position", "department", "inf_date")
    list_filter = ("position", "department", "inf_date")
    search_fields = ("last_name", "first_name", "middle_name", "inf_name")
    inlines = [EmployeeAttachmentInline]
    fieldsets = (
        (
            "Сотрудник",
            {
                "fields": (
                    "last_name",
                    "first_name",
                    "middle_name",
                    "position",
                    "department",
                    "phone_number",
                )
            },
        ),
        (
            "Информация",
            {
                "fields": (
                    "inf_name",
                    "inf_date",
                    "inf_source",
                    "audit_subject",
                    "inf_text",
                    "inf_result",
                )
            },
        ),
    )


@admin.register(EmployeeAttachment)
class EmployeeAttachmentAdmin(admin.ModelAdmin):
    list_display = ("original_name", "employee", "created_at")
    search_fields = ("original_name", "employee__last_name", "employee__first_name")
    list_select_related = ("employee",)
