from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'