# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0017_auto_20171011_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Professor',
            field=models.ManyToManyField(help_text='Enter Professors', related_name='stud_prof', to='Project.professor'),
        ),
    ]
