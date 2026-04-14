from django.db import models


class Department(models.Model):
    name = models.CharField("Подраздел", max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    last_name = models.CharField("Фамилия", max_length=100)
    first_name = models.CharField("Имя", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, blank=True)

    position = models.CharField("Должность", max_length=100, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="Подраздел", null=True,
                                   blank=True)
    phone_number = models.CharField("Номер телефона", max_length=20, blank=True)
    inf_name = models.CharField("Название", max_length=100, blank=True)
    inf_date = models.DateField("Дата заявки", null=True, blank=True)
    inf_source = models.CharField("Источник информации", max_length=100, blank=True)
    audit_subject = models.CharField("Субъект аудита", max_length=100, blank=True)
    inf_text = models.TextField("Информация", blank=True)
    inf_result = models.CharField("Результат", max_length=100, blank=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"



