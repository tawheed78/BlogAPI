from rest_framework import serializers
from .models import Post, Like, Comment

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'body', 'created_at', 'updated_at', 'likes_count','comments_data']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'body', 'created_at','user']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post','created_at']

class CommentSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Comment
        fields = ['id', 'user', 'post','body','created_at']
