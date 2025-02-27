# forms.py
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'codigo',
                'placeholder': 'Código do produto',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nome',
                'placeholder': 'Nome do produto',
            }),
            'unidade': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'unidade',
                'placeholder': 'Ex.: kg, un, litro',
            }),
            'categoria': forms.Select(choices=[
                ('Alimento', 'Alimento'),
                ('Não-Alimento', 'Não-Alimento'),
                ('Bebidas', 'Bebidas'),
            ], attrs={
                'class': 'form-control',
                'id': 'status',
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'preco',
                'placeholder': 'R$ 0,00',
            }),
            'custo': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'custo',
                'placeholder': 'Custo do produto',
            }),
            'validade': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'validade',
                    'type': 'date',
                },
                format='%Y-%m-%d'  
            ),
            'estoque': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'disponivel',
                'placeholder': 'Quantidade em estoque',
            }),
            'estoque_minimo': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'minimo',
                'placeholder': 'Estoque mínimo',
            }),
        }
