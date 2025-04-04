 
from rest_framework import viewsets, permissions
from .models import Doencas
from .serializers import DoencaSerializer

class DoencaViewSet(viewsets.ModelViewSet):
    queryset = Doencas.objects.all()
    serializer_class = DoencaSerializer
    permission_classes = [permissions.AllowAny]