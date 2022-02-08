from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app import views


router = DefaultRouter()
router.register(r'Usuario', views.UsuarioView)
router.register(r'Loja', views.LojaView)
router.register(r'Produto', views.ProdutoView)
router.register(r'Compra', views.CompraView)

urlpatterns = [
    path('', include(router.urls)),
]