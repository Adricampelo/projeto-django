from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nome',
                'placeholder': 'Nome categoria',
            })}