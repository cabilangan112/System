# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView,View,ListView
from django.views import generic
from .models import student, subject, professor

# Create your views here.


		
def ascend (request):
		queryset = student.objects.filter(Last_name__icontains='war')[:5]
		students = student.objects.all()
		context = {
			'students':students,
		
		}
		return render(request, "ascend_student_list.html", context)
		
class studentDetailView(DetailView):
	model = student
	
	template_name = "ascend_student_detail.html"

	def get_context_data(self, **kwargs):
		context = super(studentDetailView, self).get_context_data(**kwargs)
		return context
		
class  subjectList(generic.ListView):
	def get(self, request): 
		queryset = subject.objects.filter(last_name__icontains='war')[:5]
		professors = subject.objects.all()
		context = {
			'professors':professors,
		
		}
		return render(request, "ascend_professor.html", context)


class ProfessorDetailView(DetailView):
	model = professor
	
	template_name = "ascend_professor_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(ProfessorDetailView, self).get_context_data(**kwargs)
		return context
		
class SubjectDetailView(DetailView):
	model = subject
	template_name = "ascend_subject_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(SubjectDetailView, self).get_context_data(**kwargs)
		return context