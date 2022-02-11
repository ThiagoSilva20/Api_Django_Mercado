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
    path('search_usu', views.busca_usu),
    path('search_prod', views.busca_prod),
    path('search_loja', views.busca_loja),
    path('search_comp', views.busca_comp),
]