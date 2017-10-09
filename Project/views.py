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
		sub = subject.objects.exclude()
		context = {
			'students':students,
		
		}
		return render(request, "index.html", context)
		
		
def index(request):
	professors = professor.objects.all()
	context = {
	'professors':professors,
	}
	return render(request, "professor.html", context)
	
class ProfessorDetailView(DetailView):
	model = professor
	template_name = "professor_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(BookDetailView, self).get_context_data(**kwargs)
		return context