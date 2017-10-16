# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import student,Course,subject , professor,Grade






class GradeAdmin(admin.ModelAdmin):
	list_display = ( 'quiz', 'performance', 'exam', 'get_computed' )

	
class studentAdmin(admin.ModelAdmin):
	list_display = ('First_name', 'Last_name' )


admin.site.register(student,studentAdmin)
admin.site.register(Course)
admin.site.register(subject)
admin.site.register(professor)
admin.site.register(Grade,GradeAdmin)
#admin.site.register(AttendanceRecord)

