from django.db import models

class fornecedor(models.Model):

    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    produto = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
