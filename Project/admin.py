# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import student,Course,professor,subject



class subjectInline(admin.TabularInline):
	model =  subject

class subjectAdmin(admin.ModelAdmin):
	list_display = ('subject_name', 'quiz_1', 'performance_1', 'exam_1', 'grade_1', 'quiz_2', 'performance_2', 'exam_2', 'grade_2', 'quiz_3', 'performance_3', 'exam_3', 'grade_3')
	readonly_fields = ('grade_1','grade_2','grade_3')
	
class profAdmin(admin.ModelAdmin):
	list_display = ('prof_fname', 'prof_mname', 'prof_lname')

	
class studentAdmin(admin.ModelAdmin):
	list_display = ('First_name', 'Last_name')
	inlines = [subjectInline]

admin.site.register(student,studentAdmin)
admin.site.register(Course)
admin.site.register(subject,subjectAdmin)
admin.site.register(professor,profAdmin)
