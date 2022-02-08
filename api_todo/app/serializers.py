from .models import Compras, Produto, Usuario, Loja
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone']
class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id', 'nome_loja', 'cnpj', 'telefone_loja']
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome_prod', 'preco']
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ['id', 'usu', 'loja', 'prod', 'diaehora']