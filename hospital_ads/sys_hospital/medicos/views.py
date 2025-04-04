from rest_framework import viewsets, permissions
from .models import Medicos
from .serializers import MedicosSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    permission_classes = [permissions.AllowAny]