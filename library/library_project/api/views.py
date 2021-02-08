from django.shortcuts import render
from rest_framework import generics
from .serializers import *

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
