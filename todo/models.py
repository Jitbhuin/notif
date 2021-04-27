from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
