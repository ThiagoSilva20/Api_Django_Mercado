from .models import Compras, Loja, Produto, Usuario
from .serializers import CompraSerializer, UsuarioSerializer, ProdutoSerializer, LojaSerializer

##############################################

from rest_framework import viewsets

#######################################################

class UsuarioView(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

########################################

class LojaView(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

########################################

class ProdutoView(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

########################################

class CompraView(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = CompraSerializer

