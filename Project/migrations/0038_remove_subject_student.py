# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0037_auto_20171010_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='Student',
        ),
    ]
