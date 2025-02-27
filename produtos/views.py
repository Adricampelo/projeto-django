from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Produto
from django.shortcuts import get_object_or_404
from .forms import ProdutoForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

@login_required

def produtos(request):
    produtos = Produto.objects.all()  # Recupera todos os produtos do banco de dados
    return render(request, 'produtos.html', {'produtos': produtos})

# def editar(request):
#     return render(request, 'editar.html')

# def cadastrar(request):
#     return render(request, 'cadastrar.html')

# def lista_produtos(request):
#     produtos = Produto.objects.all()
#     return render(request, 'produtos.html', {'produtos': produtos})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)  # Recupera o produto pelo ID

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()  # Salva as alterações no banco
            return redirect('produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'editar.html', {'form': form, 'produto': produto})



def cadastrar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('produtos')  # Redireciona para a lista de produtos
        else:
            messages.error(request, 'Erro ao cadastrar produto. Verifique os dados.')
    else:
        form = ProdutoForm()

    return render(request, 'cadastrar.html', {'form': form})
    
# def valida_cadastro_produto(request):
#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         codigo = request.POST.get('codigo')
#         categoria = request.POST.get('categoria')
#         preco = request.POST.get('preco')
#         custo = request.POST.get('custo')
#         validade = request.POST.get('validade')
#         estoque = request.POST.get('estoque')
#         estoque_minimo = request.POST.get('estoque_minimo')
#         unidade = request.POST.get('unidade')

#         # Validações simples
#         if not all([nome, codigo, categoria, preco, validade, estoque]):
#             messages.error(request, 'Preencha todos os campos obrigatórios!')
#             return redirect('cadastrar_produto')

#         # Cria e salva o produto
#         Produto.objects.create(
#             nome=nome,
#             codigo=codigo,
#             categoria=categoria,
#             preco=preco,
#             custo=custo if custo else 0,
#             validade=validade,
#             estoque=estoque,
#             estoque_minimo=estoque_minimo if estoque_minimo else 0,
#             unidade=unidade
#         )

#         messages.success(request, 'Produto cadastrado com sucesso!')
#         return redirect('produtos')  # Redireciona para a lista de produtos

#     return redirect('produtos')

def deletar_produto(request, produto_id):
    """
    Função responsável por deletar o produto baseado no ID.
    """
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    messages.success(request, f'Produto "{produto.nome}" foi deletado com sucesso!')
    return redirect('produtos')  
