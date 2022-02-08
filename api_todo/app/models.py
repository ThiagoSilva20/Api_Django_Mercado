from django.db import models
from django.forms import CharField


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

######################################################

class Loja(models.Model):
    nome_loja = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=11)
    telefone_loja = models.CharField(max_length=11)

#######################################################

class Produto(models.Model):
    nome_prod = models.CharField(max_length=100, default='')
    preco = models.CharField(max_length=100, default=0)

#######################################################

class Compras(models.Model):   
    usu = models.ForeignKey("Usuario", on_delete=models.DO_NOTHING)
    loja = models.ForeignKey("Loja", on_delete=models.DO_NOTHING)
    prod = models.ForeignKey("Produto", on_delete=models.DO_NOTHING)
    diaehora = models.DateTimeField(auto_now_add=True)

