from django.urls import path
from .import views

urlpatterns = [
    path('relatorios', views.relatorios , name = 'relatorios'),
   

]