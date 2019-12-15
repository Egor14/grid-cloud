from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.core.files.base import ContentFile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'link', 'status', 'bytes', 'image', 'user']

    def to_representation(self, validated_data):
        print(validated_data.image.url)
        if validated_data.image.url == '/media/clustered_images/' and validated_data.status:
            validated_data.image.save(name=str(validated_data.id) + '.jpg', content=ContentFile(bytes(validated_data.bytes)))
            validated_data.bytes = b'hello'
        return validated_data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self):
        User.objects.create_user(**self.data)
