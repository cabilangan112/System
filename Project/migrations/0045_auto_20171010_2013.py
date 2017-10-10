# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0044_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Professor',
        ),
        migrations.AddField(
            model_name='subject',
            name='Professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.professor'),
        ),
    ]