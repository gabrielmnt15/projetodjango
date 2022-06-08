from pyexpat import model
from django.db import models

class nota_fiscal(models.Model):

    nome = models.CharField(max_length=100)
    cpf_comprador = models.CharField(max_length=11)
    cnpj_fornecedor = models.CharField(max_length=14)
    valor_compra = models.FloatField()
    produto = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
