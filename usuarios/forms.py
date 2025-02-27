from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'password', 'contato', 'endereco', 'cpf']
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nome',
                'placeholder': 'Nome completo do usuário',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Digite o email',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'password',
                'placeholder': 'Digite a senha',
            }),
            'contato': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contato',
                'placeholder': 'Número de contato',
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'endereco',
                'placeholder': 'Endereço completo',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'cpf',
                'placeholder': 'Digite o CPF',
            }),
        }

    
    def clean_contato(self):
        contato = self.cleaned_data.get('contato')
        if not contato.isdigit():
            raise forms.ValidationError("O número de contato deve conter apenas números.")
        return contato

    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if len(cpf) != 11 or not cpf.isdigit():
            raise forms.ValidationError("O CPF deve ter 11 dígitos numéricos.")
        return cpf

    def save(self, commit=True):
        """Sobrescreve o save() para criptografar a senha."""
        usuario = super().save(commit=False)  
        usuario.set_password(self.cleaned_data['password'])  
        if commit:
            usuario.save()  
        return usuario
