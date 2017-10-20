# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('unexcused', 'Unexcused'), ('excused', 'Excused'), ('late', 'Late')], max_length=10, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dep', models.CharField(blank=True, choices=[('c', 'Cite'), ('o', 'CBA'), ('a', 'CED'), ('r', 'Ascend')], default='c', max_length=1)),
                ('course_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.IntegerField(null=True)),
                ('performance', models.IntegerField(null=True)),
                ('exam', models.IntegerField(null=True)),
                ('Mark', models.CharField(blank=True, choices=[('f', 'Fail'), ('p', 'Pass')], default='Fail', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('bio', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_name', models.CharField(max_length=100)),
                ('First_name', models.CharField(help_text='Enter your first name ', max_length=200)),
                ('MI', models.CharField(help_text='Enter your middle Name', max_length=200)),
                ('Sex', models.CharField(blank=True, choices=[('m', 'Male'), ('o', 'Female')], default='m', max_length=1)),
                ('Course', models.ManyToManyField(related_name='student', to='ascend.Course')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ascend.Grade')),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=150)),
                ('subject_Descreption', models.CharField(max_length=200)),
                ('Professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ascend.professor')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='Subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ascend.subject'),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ascend.student'),
        ),
    ]