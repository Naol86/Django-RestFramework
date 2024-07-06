from django.urls import path
from . import views


urlpatterns = [
  path('employees/', views.EmployeeListView.as_view({'get': 'list', 'post': 'create'})),
  path('employees/<int:pk>', views.EmployeeListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
  path('positions/', views.PositionViewList.as_view({'get': 'list', 'post': 'create'})),
  path('positions/<int:pk>', views.PositionViewList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]