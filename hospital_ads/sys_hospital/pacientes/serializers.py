from rest_framework import serializers
from .models import Paciente
from enderecos.serializers import EnderecoSerializer

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'




