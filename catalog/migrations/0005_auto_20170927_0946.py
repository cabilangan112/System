# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 01:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170927_0936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_name',
            new_name='name',
        ),
    ]
