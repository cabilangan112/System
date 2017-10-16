# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0019_auto_20171011_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='Subjects',
        ),
        migrations.AddField(
            model_name='subject',
            name='Profs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prof_subject', to='Project.professor'),
        ),
    ]