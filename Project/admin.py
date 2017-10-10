# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import student,Course,subject , professor



class subjectInline(admin.TabularInline):
	model =  subject

class subjectAdmin(admin.ModelAdmin):
	list_display = ('subject_name', 'quiz', 'performance', 'exam', 'get_computed','Professor')

	
class studentAdmin(admin.ModelAdmin):
	list_display = ('First_name', 'Last_name' )
	inlines = [subjectInline]

admin.site.register(student,studentAdmin)
admin.site.register(Course)
admin.site.register(subject,subjectAdmin)
admin.site.register(professor)
