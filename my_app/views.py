from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

class BookListView(ListView):
	model = Book
	template_name= 'index.html'
