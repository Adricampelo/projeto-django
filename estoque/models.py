from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'categorias'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome
