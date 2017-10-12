# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0076_auto_20171012_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='mark',
        ),
        migrations.AddField(
            model_name='grade',
            name='Mark',
            field=models.CharField(blank=True, choices=[('f', 'fail'), ('p', 'pass')], default='p', max_length=1),
        ),
    ]
