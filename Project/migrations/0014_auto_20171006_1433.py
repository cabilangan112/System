# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0013_auto_20171006_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='exam',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='performance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='quiz',
            field=models.IntegerField(null=True),
        ),
    ]