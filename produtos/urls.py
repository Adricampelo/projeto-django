from django.urls import path
from . import views
from .views import editar_produto

urlpatterns=[
    path('produtos/', views.produtos , name = 'produtos'),
    # path('produtos/editar', views.editar , name = 'editar produtos'),
    path('editar/<int:id>/', editar_produto, name='editar_produto'),
    path('produtos/cadastrar', views.cadastrar , name = 'cadastrar produtos'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto')

]