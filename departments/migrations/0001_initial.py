# Generated by Django 4.0.1 on 2022-01-18 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название отдела')),
                ('parent_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='departments.department', verbose_name='Отдел')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='departments.department', verbose_name='Отдел')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя сотрудника')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия сотрудника')),
                ('patronymic', models.CharField(blank=True, max_length=60, null=True, verbose_name='Отчество сотрудника')),
                ('salary', models.IntegerField(verbose_name='Зарплата')),
                ('position', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='departments.position', verbose_name='Должность')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]