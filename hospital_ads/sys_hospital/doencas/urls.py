from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoencaViewSet

router = DefaultRouter()
router.register(r'doencas', DoencaViewSet, basename='doenca')

urlpatterns = [
    path('', include(router.urls)),
]