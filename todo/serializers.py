from .models import Todo
from rest_framework.serializers import ModelSerializer


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'author', 'title', 'description', 'completed')


class BasicSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title', 'completed')

