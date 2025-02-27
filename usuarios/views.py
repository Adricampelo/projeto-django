from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def login_view(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)  
                return redirect('home') 
            else:
                messages.error(request, "Usuário ou senha incorretos!")
                return redirect('login') 
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def cadastrar(request):
    storage = messages.get_messages(request)
    storage.used = True

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Funcionário cadastrado com sucesso!')
            return redirect('funcionario')  
        else:
            
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo '{field}': {error}")
    else:
        form = UsuarioForm()
        
    return render(request, 'funcionarios/cadastrar.html', {'form': form})


def funcionario(request):
    usuarios = Usuario.objects.all()  
    return render(request, 'funcionarios/funcionario.html', {'usuarios': usuarios})

def editar_funcionario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  # Salva as alterações no banco de dados
            messages.success(request, 'Funcionário atualizado com sucesso!')
            return redirect('funcionario')  # Redireciona para a lista de funcionários
        else:
            # Adiciona erros de campo específicos na mensagem
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo '{field}': {error}")
    else:
        form = UsuarioForm(instance=usuario)  # Carrega o formulário com os dados do usuário
    
    return render(request, 'funcionarios/editar.html', {'form': form, 'usuario': usuario})

def deletar_funcionario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, f'Funcionário "{usuario.nome}" foi deletado com sucesso!')
    return redirect('funcionario')

def cadastro(request):
    form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

