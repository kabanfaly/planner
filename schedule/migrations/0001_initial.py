# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workplace', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Work start time')),
                ('end_time', models.DateTimeField(verbose_name='Work end time')),
                ('break_time', models.TimeField(null=True)),
                ('day_hours', models.TimeField(null=True, verbose_name='Number of hours worked as day hours')),
                ('night_hours', models.TimeField(null=True, verbose_name='Number of hours worked as night hours')),
                ('sunday_day_hours', models.TimeField(null=True, verbose_name='Sunday: Number of hours worked as day hours')),
                ('sunday_night_hours', models.TimeField(null=True, verbose_name='Sunday: Number of hours worked as night hours')),
                ('public_day_day_hours', models.TimeField(null=True, verbose_name='Sunday: Number of hours worked as day hours')),
                ('public_day_night_hours', models.TimeField(null=True, verbose_name='Sunday: Number of hours worked as night hours')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
                ('workplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workplace.Workplace')),
            ],
        ),
    ]