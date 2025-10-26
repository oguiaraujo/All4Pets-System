from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    preco = serializers.FloatField()
    class Meta:
        model = Products
        fields = [
            'id', 'codigo', 'nome', 'descricao', 'preco',
            'estoque', 'categoria', 'data_validade', 'ativo',
            'criado_em', 'atualizado_em'
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']