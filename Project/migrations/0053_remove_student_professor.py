# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0052_auto_20171011_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Professor',
        ),
    ]
