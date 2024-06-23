from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, VideojuegoViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet, basename='empresa')
router.register(r'videojuegos', VideojuegoViewSet, basename='videojuego')

urlpatterns = [
    path('', include(router.urls)),
]
