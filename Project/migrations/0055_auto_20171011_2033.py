# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0054_auto_20171011_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Grade',
        ),
        migrations.AddField(
            model_name='student',
            name='Subject',
            field=models.ManyToManyField(related_name='student', to='Project.subject'),
        ),
    ]
