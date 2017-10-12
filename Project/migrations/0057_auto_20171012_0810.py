# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 00:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0056_auto_20171012_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade',
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.Grade'),
        ),
    ]
