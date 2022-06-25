from authentication.models import User
from django.db import models
from django.db.models.deletion import PROTECT


class Department(models.Model):
    name = models.CharField(max_length=60, verbose_name="Название отдела")
    parent_department = models.ForeignKey('self', null=True, blank=True, verbose_name="Отдел", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=60)
    department = models.ForeignKey(Department, null=True, blank=True, verbose_name="Отдел", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class DepartmentPermission(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    TYPES = (
        ('Привелегии', 1),
        ('Сотрудники - только чтение', 2),
        ('Сотрудники - полный доступ', 3),
    )
    type = models.PositiveIntegerField(choices=TYPES)
    read_only = models.BooleanField(null=False, blank=False, verbose_name="Только для чтения", default=True)
    department = models.ForeignKey(Department, null=False, blank=False, verbose_name="Отдел", on_delete=models.CASCADE)


class Employee(models.Model):
    position = models.ForeignKey(Position, on_delete=PROTECT, null=True,  verbose_name="Должность")
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    salary = models.IntegerField(verbose_name="Зарплата")

    def __str__(self):
        return self.name

    def _do_insert(self, manager, using, fields, returning_fields, raw):
        return super()._do_insert(manager, using, fields, returning_fields, raw)
