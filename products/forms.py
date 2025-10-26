from django import forms
from .models import Products  

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'codigo',
            'nome',
            'descricao',
            'preco',
            'estoque',
            'categoria',
            'data_validade',
        ]  
