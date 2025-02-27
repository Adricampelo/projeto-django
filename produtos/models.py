from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    codigo = models.CharField(max_length=50)
    validade = models.DateField()
    unidade = models.CharField(max_length=50, blank=True, null=True)
    custo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque_minimo = models.IntegerField(default=0, blank=True, null=True)


    class Meta:
        db_table = 'produtos_produto'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome
