from django.urls import path
from .import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),  
    path('cadastro/', views.cadastro, name='cadastro'),
    path('funcionario/', views.funcionario, name='funcionario'),
    path('funcionario/cadastrar/', views.cadastrar, name='cadastrar_funcionario'),
    path('editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('deletar/<int:usuario_id>/', views.deletar_funcionario, name='deletar_funcionario'),
    # path('logout/', views.logout_view, name='logout'),  # Redireciona para a função logout
]
