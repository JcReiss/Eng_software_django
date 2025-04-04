from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('enderecos.urls')),
    path('api/', include('pacientes.urls')),
    path('api/', include('especializacoes.urls')),
    path('api/', include('doencas.urls')),
    path('api/', include('enfermeiros.urls')),
    path('api/', include('medicos.urls')),
]
