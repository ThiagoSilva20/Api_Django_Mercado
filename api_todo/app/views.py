from .models import Compras
from urllib import response
from .serializers import ComprasSerializer

##############################################

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound

#######################################################

class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer
#######################################################################################

class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compras.objects.all()
    serializer_class = ComprasSerializer
#######################################################################################