from rest_framework import viewsets, permissions
from .models import Endereco
from .serializers import EnderecoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [permissions.AllowAny]