from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnderecoViewset

router = DefaultRouter()
router.register(r'enderecos', EnderecoViewset,basename='Endereco')

urlpatterns = [
    path('', include(router.urls)),
]
