from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "last_name",
            "first_name",
            "middle_name",
            "position",
            "department",
            "phone_number",
            "inf_name",
            "inf_date",
            "inf_source",
            "audit_subject",
            "inf_text",
            "inf_result",
        ]
        widgets = {
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "middle_name": forms.TextInput(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-select"}),
            "department": forms.Select(attrs={"class": "form-select"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),

            "inf_name": forms.TextInput(attrs={"class": "form-control"}),
            "inf_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "inf_source": forms.TextInput(attrs={"class": "form-control"}),
            "audit_subject": forms.TextInput(attrs={"class": "form-control"}),

            "inf_text": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "inf_result": forms.TextInput(attrs={"class": "form-control"}),
        }
