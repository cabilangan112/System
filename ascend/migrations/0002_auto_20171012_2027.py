# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ascend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Dep',
            field=models.CharField(blank=True, choices=[('c', 'CBA')], default='c', max_length=1),
        ),
    ]
