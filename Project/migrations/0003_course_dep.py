# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_auto_20170930_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Dep',
            field=models.CharField(blank=True, choices=[('c', 'Cite'), ('o', 'CBA'), ('a', 'CED'), ('r', 'Ascend')], default='c', max_length=1),
        ),
    ]
