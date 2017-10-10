# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0032_auto_20171010_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='Student',
        ),
        migrations.AddField(
            model_name='professor',
            name='Subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.subject'),
        ),
    ]
