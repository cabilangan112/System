# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0048_auto_20171010_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Professor',
            field=models.ManyToManyField(related_name='student', to='Project.Grade'),
        ),
    ]
