from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

#Operações CRUD

class ListToDo(generics.ListAPIView): # List
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView): # Detail
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class CreateToDo(generics.CreateAPIView): # Create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DeleteToDo(generics.DestroyAPIView): # Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
def todo_frontend(request):
    return render(request, 'index.html')

