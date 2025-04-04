from rest_framework import serializers
from .models import Doencas

class DoencaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doencas
        fields = '__all__'	