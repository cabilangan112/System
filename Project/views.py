# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.views.generic import DetailView,View,ListView
from django.views import generic
from .forms import StudentForm
from .models import student, subject, professor

# Create your views here.



def index(request):
		queryset = student.objects.filter(Last_name__icontains='cabilangan')[:5]
		students = student.objects.all()
		context = {
			'students':students,
		
		}
		return render(request, "student_list.html", context)
		
		
class Student(View):
	def get(self, request):
		students = student.objects.all()
		context = {
			'students' : students,
			'form' : StudentForm,
		}
		return render(request, "student-form.html", context)

	def post(self, request):
		form = StudentForm(request.POST)
		students = student.objects.all()
		
		if form.is_valid():
			form.save()
			return redirect('student')
			
		context = {
			'form' : form,
			'students' : students,
		}
		
		return render(request, "student-form.html", context)
	
class studentDetailView(DetailView):
	model = student
	
	template_name = "student_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(studentDetailView, self).get_context_data(**kwargs)
		return context
		
class  subjectList(generic.ListView):
	def get(self, request): 
		queryset = subject.objects.filter(course__icontains='BSCS')[:5]
		professors = subject.objects.all()
		context = {
			'professors':professors,
		
		}
		return render(request, "professor.html", context)


class ProfessorDetailView(DetailView):
	model = professor
	
	template_name = "professor_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(ProfessorDetailView, self).get_context_data(**kwargs)
		return context
		
class SubjectDetailView(DetailView):
	model = subject
	template_name = "subject_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(SubjectDetailView, self).get_context_data(**kwargs)
		return context