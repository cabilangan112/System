# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0020_auto_20171011_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Professor',
        ),
    ]