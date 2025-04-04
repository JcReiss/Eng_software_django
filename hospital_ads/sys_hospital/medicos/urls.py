from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicosViewSet

router = DefaultRouter()
router.register(r'medicos', MedicosViewSet, basename='medico')

urlpatterns = [
    path('', include(router.urls)),
]