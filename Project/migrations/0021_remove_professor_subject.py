# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 01:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0020_professor_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='Subject',
        ),
    ]
