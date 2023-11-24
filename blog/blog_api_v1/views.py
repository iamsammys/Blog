from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
)
from blog_app.models import Post
from blog_api_v1.serializers import PostSerializers


class PostListApiView(ListCreateAPIView):
    """Generic class-based view for a list of posts.

    Attributes:
        queryset: queryset for PostListApiView
        serializer_class: serializer_class for PostListApiView
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostCreateApiView(CreateAPIView):
    """Generic class-based view for creating a post.

    Attributes:
        queryset: queryset for PostCreateApiView
        serializer_class: serializer_class for PostCreateApiView
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers