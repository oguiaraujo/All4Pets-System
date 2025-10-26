from django.db import models
from decimal import Decimal

class Products(models.Model):
    codigo = models.CharField(max_length=20, unique= True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'),
        null=False,
        blank=False
    )
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length = 50)
    data_validade = models.DateField(null=True, blank= True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add= True)
    atualizado_em = models.DateTimeField(auto_now= True)

    class Meta:
        
        verbose_name = "Product" 
        verbose_name_plural = "Products" 
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.codigo} - {self.nome}"