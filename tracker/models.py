from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeField

from departments.models import Employee


class WorkCategory(models.Model):
    name = models.CharField(max_length=60, verbose_name="Категория работы")
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class WorkType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип работы")
    description = models.TextField(max_length=200, blank=True, verbose_name="Описание")
    category = models.ForeignKey(WorkCategory, on_delete=PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.name


class TimeLine(models.Model):
    start_at = DateTimeField()
    end_at = DateTimeField()
    comment = models.TextField(max_length=200, blank=True, verbose_name="Описание")
    employee = models.ForeignKey(Employee, on_delete=PROTECT)
    work_type = models.ForeignKey(WorkType, on_delete=PROTECT)

    def __str__(self):
        return '%s, %s' % (self.start_at, self.end_at)
