from django.shortcuts import render
from rest_framework import viewsets
from .serializsers import EmployeeSerializer, PositionSerializer
from .models import Employee, Position

# Create your views here.

class EmployeeListView(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

class PositionViewList(viewsets.ModelViewSet):
  queryset = Position.objects.all()
  serializer_class = PositionSerializer