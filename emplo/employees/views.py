from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializsers import EmployeeSerializer, PositionSerializer
from .models import Employee, Position


# Create your views here.

class EmployeeListView(viewsets.ModelViewSet):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer
  lookup_field = 'pk'


class PositionViewList(viewsets.ModelViewSet):
  queryset = Position.objects.all()
  serializer_class = PositionSerializer