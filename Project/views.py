# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView,View,ListView
from django.views import generic
from .models import student, subject

# Create your views here.

class studentListView(generic.ListView):

	def get(self, request): 
		students = student.objects.all()
		subs = subject.objects.exclude()
		context = {
			'students':students,
			'sub ':subs ,
		}
		return render(request, "index.html", context)