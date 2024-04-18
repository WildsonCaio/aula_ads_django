from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(decimal_places=2, max_digits=9)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    codigo = models.CharField(max_length=12)
    em_estoque = models.BooleanField()
    data_criacao = models.DateField()

    def __str__(self):
        return self.nome