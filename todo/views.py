from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import TodoSerializer, BasicSerializer
from .models import Todo
from notifications.signals import notify


class ListTodo(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        notify.send(self.request.user, recipient=instance.author, verb='new task created')


class CompletedListTodo(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all().filter(completed=True)
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        notify.send(self.request.user, recipient=self.request.user, verb='new task created')


class AssignedListTodo(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all().filter(completed=False)
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        notify.send(self.request.user, recipient=self.request.user, verb='new task created')


class DetailTodo(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_update(self, serializer):
        print(self.request.POST)
        instance = serializer.save()
        print(instance.author)
        notify.send(self.request.user, recipient=instance.author, verb='updated')

    def perform_destroy(self, serializer):
        instance = serializer.save()
        notify.send(self.request.user, recipient=instance.author, verb='Deleted')

