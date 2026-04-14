from django import forms
from .models import Employee


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return [single_file_clean(data, initial)] if data else []


class EmployeeForm(forms.ModelForm):
    attachments = MultipleFileField(
        required=False,
        widget=MultipleFileInput(attrs={"class": "form-control"}),
        label="Вложения",
    )

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
            "position": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-select"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "inf_name": forms.TextInput(attrs={"class": "form-control"}),
            "inf_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "inf_source": forms.TextInput(attrs={"class": "form-control"}),
            "audit_subject": forms.TextInput(attrs={"class": "form-control"}),
            "inf_text": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "inf_result": forms.TextInput(attrs={"class": "form-control"}),
        }
