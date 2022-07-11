from django.urls import path, include 

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('session/<int:session_id>/', views.session, name="session_id")
]