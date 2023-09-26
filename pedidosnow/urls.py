from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, 

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apppedidosnow.views import (
    PedidoViewSet,
    CategoriaViewSet,
    ProdutoViewSet,
    )
from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from apppedidosnow.views import CategoriaViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"pedidos", PedidoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]