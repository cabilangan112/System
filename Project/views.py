# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView,View

# Create your views here.

class BookListView(generic.ListView):

	def get(self, request):
		queryset = Book.objects.filter(title__icontains='war')[:5] 
		books = Book.objects.all()
		paginate_by = 2
		context = {
			'books': books,
		}
		return render(request, "book_list.html", context)