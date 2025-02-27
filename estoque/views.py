from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categoria
from .forms import CategoriaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required

# def categorias(request):
#     return render(request, 'categorias.html')

# def cadastrar(request):
#     return render(request, 'cadastrarcat.html')

def editar(request):
    return render(request, 'editarcat.html')


def categorias(request):
    categorias = Categoria.objects.all()  # Recupera todas as categorias do banco de dados
    return render(request, 'categorias.html', {'categorias': categorias})


def cadastrar(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')  # Redireciona para a lista de categorias
    else:
        form = CategoriaForm()

    return render(request, 'cadastrarcat.html', {'form': form})


def editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)  # Busca a categoria pelo ID

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)  # Preenche o formulário com a categoria
        if form.is_valid():
            form.save()  # Salva a categoria editada
            return redirect('categorias')  # Redireciona para a lista de categorias
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'editarcat.html', {'form': form})  # Passa o formulário para o template

def deletar_categoria(request, categoria_id):
    """
    Função responsável por deletar o categorias baseado no ID.
    """

    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    messages.success(request, f'Categoria "{categoria.nome}" foi deletado com sucesso!')
    return redirect('categorias')  
