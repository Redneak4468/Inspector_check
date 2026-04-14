from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_position_to_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeAttachment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.FileField(upload_to="employee_files/%Y/%m/%d/", verbose_name="Файл")),
                ("original_name", models.CharField(max_length=255, verbose_name="Имя файла")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="core.employee",
                        verbose_name="Сотрудник",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вложение",
                "verbose_name_plural": "Вложения",
                "ordering": ["-created_at"],
            },
        ),
    ]
