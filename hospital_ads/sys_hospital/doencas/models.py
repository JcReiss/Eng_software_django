from django.db import models

class Doencas(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField("")
    sintomas = models.TextField("")
    tratamentos = models.TextField("")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'doencas'

    def __str__(self):
        return self.nome