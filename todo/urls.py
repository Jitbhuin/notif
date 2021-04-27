from django.urls import path
from .views import DetailTodo,CompletedListTodo,AssignedListTodo,ListTodo
urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('completed', CompletedListTodo.as_view()),
    path('assigned', AssignedListTodo.as_view()),
]