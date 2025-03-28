from django.db import models

class Endereco(models.Model):
    cep = models.CharField(max_length=8)  
    logradouro = models.CharField(max_length=100) 
    numero = models.CharField(max_length=10)  
    complemento = models.CharField(max_length=50, blank=True, null=True)  
    bairro = models.CharField(max_length=50)  
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2) 
    data_criacao = models.DateTimeField(auto_now_add=True)  
    data_atualizacao = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'enderecos'

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"