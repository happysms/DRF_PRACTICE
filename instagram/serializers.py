from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class PostSerializer(ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    # author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            'pk',
            'author_username',
            'message',
            'created_at',
            'updated_at',
            'is_public',
        ]

