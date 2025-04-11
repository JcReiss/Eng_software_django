from django.db import models

class Consultas(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=225)
    ativo = models.BooleanField(default=True) 
    data_criacao = models.DateTimeField(auto_now_add=True)  
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'consultas'

    def __str__(self):
        return self.nome    