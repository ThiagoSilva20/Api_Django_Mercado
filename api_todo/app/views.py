from app.models import Todo
from app.serializers import TodoSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoListAndCreate(APIView):
    def get(self, request):
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailChangeAndDelete(APIView):

    def get_object(self, request,pk):
        try:
            todo = self.get_object(pk)
        except Todo.DoesNotExist:
            raise NotFound()
    
    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer .errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):        
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

