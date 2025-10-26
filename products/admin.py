from django.contrib import admin
from .models import Products
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'estoque', 'categoria', 'data_validade', 'ativo')
    list_filter = ('ativo', 'categoria')
    search_fields = ('nome', 'codigo', 'descricao') 
    list_editable = ('preco', 'estoque', 'ativo') 
    ordering = ('nome',) 

admin.site.register(Products, ProductsAdmin)
