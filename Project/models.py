# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse 

from django.db import models


class student(models.Model):
	Subject		 = 	 models.ForeignKey('subject', on_delete=models.SET_NULL, null=True)
	Last_name    =	 models.CharField(max_length=100)
	First_name 	 = 	 models.CharField(max_length=200, help_text="Enter your first name ")
	MI 			 =	 models.CharField(max_length=200, help_text="Enter your middle Name")
	
	Gender = (
        ('m', 'Male'),
        ('o', 'Female'),
	)
	Sex			  =   models.CharField(max_length=1, choices=Gender, blank=True, default='m')
	Professor		 = 		models.ForeignKey('professor', on_delete=models.SET_NULL, null=True)
	
	Course		  =   models.ManyToManyField("Course", related_name="student") 
	grade	     = 		models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)
	

	

	def get_absolute_url(self):
		return reverse(' student-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)
		
class Meta:
        ordering = ['Course']

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

	subject_name		 = 		models.CharField(max_length=150)
	subject_Descreption  = 	 	models.CharField(max_length=200)	

	

	def __str__(self):
		return self.subject_name
	
	
		
class Grade(models.Model):
	
	Subject		 = 	 	models.ForeignKey('subject', on_delete=models.SET_NULL, null=True)
	
	quiz		 = 		models.IntegerField(null=True)
	performance	 =	    models.IntegerField(null=True)
	exam         =      models.IntegerField(null=True)
	mark = (
			('f', 'Fail'),
			('p', 'Pass'),

	)
	Mark = models.CharField(max_length=1, choices=mark, blank=True, default='Fail')
	

	def get_computed(self):
		result = self.quiz * 0.25 + self.performance * 0.25 + self.exam  * 0.50 
		return result

	def save(self, *args, **kwargs):
		self.computed = self.get_computed()
		super(Grade, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.Mark
	
	def get_absolute_url(self):
		return reverse('subject-detail', args=[str(self.id)])
		
		

class professor(models.Model):
	
	first_name		= models.CharField(max_length=150)
	last_name 		= models.CharField(max_length=150)
	bio 			= models.TextField(max_length=300)
	
	def get_absolute_url(self):
		return reverse('professor-detail', args=[str(self.id)])
		
	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)
		
		
		
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
    meeting 		= models.DateField(null=True, blank=True)
    student	 		= models.ForeignKey(student)
    status  		= models.CharField("", max_length=10, choices=ATTENDANCE_TYPES)
 
    def __unicode__(self):
        return "%s %s was %s %s %s" % (self.student.Last_name,  self.status, ATTENDANCE_PRONOUNS[self.status], self.meeting)
		
		
