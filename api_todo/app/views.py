from rest_framework.response import Response
from .models import Compras, Loja, Produto, Usuario
from .serializers import CompraSerializer, UsuarioSerializer, ProdutoSerializer, LojaSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request

########################################

from rest_framework import viewsets


########################################

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

########################################
@api_view(['GET'])
def busca_usu(request):
    str_busca = request.GET['usuario']
    frela = Usuario.objects.filter(nome=str_busca)
    print(frela)

    frela2 = UsuarioSerializer(frela, many=True).data
    return Response(data=frela2)

########################################
@api_view(['GET'])
def busca_prod(request):
    str_busca = request.GET['produto']
    frela = Produto.objects.filter(nome_prod=str_busca)
    print(frela)

    frela2 = ProdutoSerializer(frela, many=True).data
    return Response(data=frela2)

########################################
@api_view(['GET'])
def busca_loja(request):
    str_busca = request.GET['loja']
    frela = Loja.objects.filter(nome_loja=str_busca)
    print(frela)

    frela2 = LojaSerializer(frela, many=True).data
    return Response(data=frela2)
