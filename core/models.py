from django.db import models


class Position(models.Model):
    name = models.CharField("Должность", max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField("Подраздел", max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    last_name = models.CharField("Фамилия", max_length=100)
    first_name = models.CharField("Имя", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, blank=True)

    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name="Должность")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="Подраздел")
    email = models.EmailField("Почта", blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
