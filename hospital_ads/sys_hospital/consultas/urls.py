from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultasViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultasViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls)),
]