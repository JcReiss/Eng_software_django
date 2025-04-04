from rest_framework import serializers
from .models import Especializacoes

class EspecializacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especializacoes
        fields = '__all__'	