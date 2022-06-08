from django.db import models

class produto(models.Model):
    
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    valor = models.FloatField()
    quantidade = models.IntegerField()
    classe = models.CharField(max_length=100)

    def __str__(self):
        return self.nome