# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView,View,ListView
from django.views import generic
from .models import student, subject, professor

# Create your views here.

class studentListView(generic.ListView):

	def get(self, request): 
		students = student.objects.all()
		context = {
			'students':students,
		
		}
		return render(request, "student_list.html", context)
		
		
def index(request):
		queryset = subject.objects.filter(subject_name__icontains='war')[:5]
		subjects = subject.objects.all()
		context = {
			'subjects':subjects,
		
		}
		return render(request, "index.html", context)


class ProfessorDetailView(DetailView):
	model = professor
	template_name = "professor_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(BookDetailView, self).get_context_data(**kwargs)
		return context