from blog_app.models import Post
from rest_framework import serializers


class PostSerializers(serializers.ModelSerializer):
    """Serializer for Post model
    
    Attributes:
        serializers.ModelSerializer: serializer for Post model
    """
    class Meta:
        model = Post
        fields = ("title", "content", "author", "created_at")