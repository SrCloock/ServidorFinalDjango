from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from main.views import EmpresaViewSet, VideojuegoViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'videojuegos', VideojuegoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # URL para obtener tokens JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # URL para renovar tokens JWT
    path('api/', include(router.urls)),  # Incluir las URLs de la app main bajo /api/
]
