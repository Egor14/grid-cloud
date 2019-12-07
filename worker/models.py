from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    input_data = models.CharField(max_length=100)
    status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
