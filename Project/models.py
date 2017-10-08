# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse 

from django.db import models


class student(models.Model):
	Last_name    =	 models.CharField(max_length=100)
	First_name 	 = 	 models.CharField(max_length=200, help_text="Enter your first name ")
	MI 			 =	 models.CharField(max_length=200, help_text="Enter your middle Name")

	Gender = (
        ('m', 'Male'),
        ('o', 'Female'),
	)
	Sex			  =   models.CharField(max_length=1, choices=Gender, blank=True, default='m')
	
	course		  =   models.ManyToManyField("Course", related_name="student")



	def get_absolute_url(self):
		return reverse(' student-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)
		
		

class Meta:
        ordering = ['Last_name']

class Course(models.Model):
	Department = (
			('c', 'Cite'),
			('o', 'CBA'),
			('a', 'CED'),
			('r', 'Ascend'),
	)
	Dep = models.CharField(max_length=1, choices=Department, blank=True, default='c')
	
	
	course_name  	=  models.CharField(max_length=100)
	description 	=  models.TextField(max_length=500)
	
	
	
	def __str__(self):
		return self.course_name

		return "{} Courses {}" .format(self.course_name, self.list_subjects())
		
	def list_subjects(self):
		return ",".join([subject.subject_name for subject in self.subjects.all()])

	def save(self, *args, **kwargs):
	
		super(Course, self).save(*args, **kwargs)
		
class subject(models.Model):
	subject_name = 		models.CharField(max_length=150)
	quiz		 = 		models.IntegerField(null=True)
	performance	 =	    models.IntegerField(null=True)
	exam         =      models.IntegerField(null=True)
	Student      =      models.ForeignKey('student', on_delete=models.SET_NULL, null=True)
 
	def get_computed(self):
		result = self.quiz * 0.25 + self.performance * 0.25 + self.exam  * 0.50 
		return result

	def save(self, *args, **kwargs):
		self.computed = self.get_computed()
		super(subject, self).save(*args, **kwargs)

 
	def __str__(self):
		return self.subject_name
	
	def get_absolute_url(self):
		return reverse('subject-detail', args=[str(self.id)])
		
		
ATTENDANCE_TYPES = (
    ('present', 'Present'),
    ('unexcused', 'Unexcused'),
    ('excused', 'Excused'),
    ('late', 'Late'),
)

ATTENDANCE_PRONOUNS = {
    'present': 'at',
    'unexcused': 'from',
    'excused': 'from',
    'late': 'to',
    '': '',
}

class AttendanceRecord(models.Model):
    meeting = models.DateField(null=True, blank=True)
    student = models.ForeignKey(student)
    status = models.CharField("", max_length=10, choices=ATTENDANCE_TYPES)
 
    def __unicode__(self):
        return "%s %s was %s %s %s" % (self.student.Last_name,  self.status, ATTENDANCE_PRONOUNS[self.status], self.meeting)

