from rest_framework import viewsets, permissions
from .models import Consultas
from .serializers import ConsultasSerializer

class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
    permission_classes = [permissions.AllowAny]  