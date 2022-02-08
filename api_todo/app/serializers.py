from .models import Compras, Produto, Usuario, Loja
from rest_framework import serializers

class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'telefone']
class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id', 'nome_loja', 'cnpj', 'telefone_loja']
class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome_prod', 'preco']
class ComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ['id', 'usu', 'loja', 'prod', 'diaehora']