from django.urls import path
from .import views

urlpatterns = [
    path('estoque/categorias', views.categorias, name='categorias'),  # Página de listagem de categorias
    path('estoque/categorias/cadastrar', views.cadastrar, name='cadastrar_categorias'),  # Página para cadastrar categoria
    path('estoque/categorias/editar/<int:id>/', views.editar, name='editar_categorias'),  # Página para editar categoria
    path('estoque/categorias/deletar/<int:categoria_id>/', views.deletar_categoria, name='deletar_categoria')
]


