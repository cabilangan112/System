# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import student,Course,subject , professor,Grade, AttendanceRecord, StudentAttendance

class GradeAdmin(admin.ModelAdmin):
	list_display = ( 'quiz', 'performance', 'exam', 'get_computed' )

	
class studentAdmin(admin.ModelAdmin):
    list_display = ('Last_name', 'First_name', 'MI', 'Sex','Professor','course','grade',)
    fields = ['First_name', 'Last_name', ('MI', 'Sex','Professor', 'course','grade',)]



admin.site.register(student,studentAdmin)
admin.site.register(Course)
admin.site.register(subject)
admin.site.register(professor)
admin.site.register(Grade,GradeAdmin)
admin.site.register(AttendanceRecord)

admin.site.register(StudentAttendance)

