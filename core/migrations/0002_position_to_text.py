from django.db import migrations, models


def copy_position_names(apps, schema_editor):
    Employee = apps.get_model("core", "Employee")
    Position = apps.get_model("core", "Position")

    position_map = {str(p.id): p.name for p in Position.objects.all()}
    for employee in Employee.objects.all().only("id", "position", "position_text"):
        raw_position = getattr(employee, "position", None)
        if raw_position is None:
            employee.position_text = ""
        else:
            position_id = getattr(raw_position, "id", raw_position)
            employee.position_text = position_map.get(str(position_id), "")
        employee.save(update_fields=["position_text"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="position_text",
            field=models.CharField(blank=True, default="", max_length=100, verbose_name="Должность"),
            preserve_default=False,
        ),
        migrations.RunPython(copy_position_names, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="employee",
            name="position",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="position_text",
            new_name="position",
        ),
        migrations.DeleteModel(
            name="Position",
        ),
    ]
