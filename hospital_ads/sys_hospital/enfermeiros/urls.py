from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnfermeirosViewSet

router = DefaultRouter()
router.register(r'enfermeiros', EnfermeirosViewSet, basename='enfermeiro')

urlpatterns = [
    path('', include(router.urls)),
]