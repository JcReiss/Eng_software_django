from rest_framework import serializers
from .models import Enfermeiros

class EnfermeirosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiros
        fields = '__all__'