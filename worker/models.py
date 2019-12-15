from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    bytes = models.BinaryField(max_length=1000000, default=b'hello')
    image = models.ImageField(upload_to='clustered_images/', default='clustered_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

