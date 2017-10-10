# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0036_remove_professor_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='course',
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(related_name='student', to='Project.professor'),
        ),
    ]