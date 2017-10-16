# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse 

from django.db import models


class student(models.Model):
	First_name = models.CharField(max_length=200, help_text="Enter your first name ")
	Middle_name = models.CharField(max_length=200, help_text="Enter your middle Name")
	Last_name = models.CharField(max_length=100,help_text="Enter your last name ")
	#Professor = models.ManyToManyField("professor", related_name="stud_prof",help_text="Enter Professors")
	#subject = models.ManyToManyField("Subject", related_name="grade")
	#subject = models.ForeignKey('subject')

	#Gender List
	Gender = (
        ('m', 'Male'),
        ('o', 'Female'),
	)
	Gender = models.CharField(max_length=1, choices=Gender, blank=True, default='m')
	
	course = models.ManyToManyField("Course", related_name="student")

	#def get_absolute_url(self):
	#	return reverse(' student-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)

		
		

class Meta:
        ordering = ['Last_name']

class Course(models.Model):
	#Department list
	Department = (
			('c', 'Cite'),
			('o', 'CBA'),
			('a', 'CED'),
			('r', 'Ascend'),
	)
	Dep = models.CharField(max_length=1, choices=Department, blank=True, default='c')
	
	course_name = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	
	
	
	def __str__(self):
		return self.course_name

		return "{} Courses {}" .format(self.course_name, self.list_subjects())
		
	def list_subjects(self):
		return ",".join([subject.subject_name for subject in self.subjects.all()])

	def save(self, *args, **kwargs):
		super(Course, self).save(*args, **kwargs)
		
		
class professor(models.Model):
	prof_fname = models.CharField(max_length=100)
	prof_mname = models.CharField(max_length=100)
	prof_lname = models.CharField(max_length=100)
	
	def __str__(self):
		#display full prof name
		return "Prof."+ " " + self.prof_fname + " "+ self.prof_lname
		
	def list_students(self):
		return ",".join([professor.prof_lname for professor in self.prof.all()])
		
	def save(self, *args, **kwargs):
		super(professor, self).save(*args, **kwargs)
		
		
		
class subject(models.Model):
	subject_name = models.CharField(max_length=150)
	quiz_1 = models.IntegerField("Trinal Quiz",null=True)
	performance_1 = models.IntegerField("Trinal Performance",null=True)
	exam_1 = models.IntegerField("Trinal Exam",null=True)
	
	quiz_2 = models.IntegerField("Midterm Quiz",null=True)
	performance_2 = models.IntegerField("Midterm Performance",null=True)
	exam_2 = models.IntegerField("Midterm Exam",null=True)
	
	quiz_3 = models.IntegerField("Final Quiz",null=True)
	performance_3 = models.IntegerField("Final Performance",null=True)
	exam_3 = models.IntegerField("Final Exam",null=True)
	
	Student = models.ForeignKey('student', on_delete=models.SET_NULL, null=True,related_name="grade")
	Professor = models.ForeignKey('professor', on_delete=models.SET_NULL, null=True,related_name="prof_subject")
 
	def __str__(self):
		return self.subject_name
		
	def _get_total_1(self):
		#quiz=25% performance=25% exam=50%
		return (self.quiz_1 * 0.25) + (self.performance_1 * 0.25 ) + (self.exam_1 * 0.50)
	grade_1 = property(_get_total_1)
	
	def _get_total_2(self):
		#quiz=25% performance=25% exam=50%
		return (self.quiz_2 * 0.25) + (self.performance_2 * 0.25 ) + (self.exam_2 * 0.50)
	grade_2 = property(_get_total_2)
	
	def _get_total_3(self):
		#quiz=25% performance=25% exam=50%
		return (self.quiz_3 * 0.25) + (self.performance_3 * 0.25 ) + (self.exam_3 * 0.50)
	grade_3 = property(_get_total_3)
	
	def save(self, *args, **kwargs):
		super(subject, self).save(*args, **kwargs)
	
	
	
	#def get_absolute_url(self):
	#	return reverse('subject-detail', args=[str(self.id)])

