from rest_framework import viewsets, permissions
from .models import Enfermeiros
from .serializers import EnfermeirosSerializer

class EnfermeirosViewSet(viewsets.ModelViewSet):
    queryset = Enfermeiros.objects.all()
    serializer_class = EnfermeirosSerializer
    permission_classes = [permissions.AllowAny]
