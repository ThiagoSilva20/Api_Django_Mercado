from rest_framework.response import Response
from .models import Compras, Loja, Produto, Usuario
from .serializers import CompraSerializer, UsuarioSerializer, ProdutoSerializer, LojaSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request

##############################################

from rest_framework import viewsets


#############################################

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

#############################################

@api_view(['GET'])
def busca(request):
    print(request)
    str_busca = request.GET['usuario']
    print(str_busca)

    return Response(data=str_busca)
