from django.urls import path
from . import views


urlpatterns = [
  path('employees/', views.EmployeeListView.as_view({'get': 'list', 'post': 'create'})),
  path('positions/', views.PositionViewList.as_view({'get': 'list', 'post': 'create'})),
]