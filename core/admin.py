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
    list_display = ("last_name", "first_name", "middle_name", "position", "department")
    list_filter = ("position", "department")
    search_fields = ("last_name", "first_name", "middle_name")
