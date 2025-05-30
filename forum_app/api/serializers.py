from rest_framework import serializers
from forum_app.models import Post, Comment, User


class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    created_at = serializers.DateField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    created_at = serializers.DateField(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'