# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0059_subject_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Project.Grade'),
        ),
    ]
