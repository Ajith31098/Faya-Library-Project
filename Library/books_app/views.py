from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer
