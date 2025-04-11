from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from pacientes.views import PacienteViewSet
from enderecos.views import EnderecoViewSet
from consultas.views import ConsultasViewSet
from doencas.views import DoencaViewSet
from enfermeiros.views import EnfermeirosViewSet
from medicos.views import MedicosViewSet

router = DefaultRouter()
router.register(r'api/pacientes', PacienteViewSet)  
router.register(r'api/enderecos', EnderecoViewSet) 
router.register(r'api/consultas', ConsultasViewSet)
router.register(r'api/doencas', DoencaViewSet)
router.register(r'api/enfermeiros', EnfermeirosViewSet)
router.register(r'api/medicos', MedicosViewSet)    
 

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', include(router.urls)),  
]



