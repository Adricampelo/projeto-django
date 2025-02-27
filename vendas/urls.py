from django.urls import path
from .import views

urlpatterns = [
    path('pdv', views.pdv , name = 'pdv'),
     path('vendas', views.vendas , name = 'vendas'),
    

]