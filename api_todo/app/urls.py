from app.views import TodoListAndCreate, TodoDetailChangeAndDelete
from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view())
]