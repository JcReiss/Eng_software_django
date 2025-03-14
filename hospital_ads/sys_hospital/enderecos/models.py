from django.db import models

class Endereco(models.Model):
    logadouro = models.CharField(max_length=250)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairo = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f"(self.logadouro), (self.numero) - (self.cidade)/(self.estado)"
    