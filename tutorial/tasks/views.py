from django.shortcuts import render        #Imports the 'render' function from Django's module to render html files.
from rest_framework import generics   #imports the generics module to provide a set of generic views for building API endpoints.
from .models import Task    #imports the Task model from the current module.
from .serializers import TaskSerializer  #imports the TaskSerializer from the current module.

# Create your views here.

class TaskListCreateAPIView(generics.ListCreateAPIView): #Defines a class-based view for listing and creating tasks using the 'GET' and 'POST' tasks respectively.
    queryset = Task.objects.all()  #Setting the queryset to retrieve all Task objects from the database
    serializer_class = TaskSerializer  # sets the serializer_class attribute of the TaskListCreateAPIView class to TaskSerializer, indicating that Task objects should be serialized using the TaskSerializer class.
  
class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):   #Defining a class-based view for retrieving, updating, and deleting tasks using the 'GET', 'PUT'and 'DELETE' tasks.
    queryset = Task.objects.all()    #Setting the queryset to retrieve all Task objects from the database
    serializer_class = TaskSerializer  # sets the serializer_class attribute of the TaskRetrieveUpdateDestroyAPIView class to TaskSerializer, indicating that Task objects should be serialized using the TaskSerializer class.
