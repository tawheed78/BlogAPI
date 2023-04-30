from django.contrib.auth.models import User
from rest_framework import generics
from .models import Post, Like, Comment
from .serializers import PostSerializer, PostCreateSerializer,CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .utils import IsOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostContentFilter
    
class UserPostAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = PostSerializer

    def get(self, request, username):
        user = User.objects.filter(username=username).first()
        if not user:
            return Response(status=404)
        posts = Post.objects.filter(user = request.user)
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data, status=200)

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, AllowAny]

class PostSearchAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostContentFilter
    
class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [ IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def perform_create(self, serializer):
        serializer.user = self.request.user
        serializer.save()
    

class PostDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwner]

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner, IsAuthenticated]

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwner,IsAuthenticated]

class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
    
    def post(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if not post:
            return Response(status=404)
        liked = post.likes.all().values_list('user', flat= True)
        if request.user.id in liked:
            post.likes_count -= 1
            post.likes.filter(user = request.user).delete()
        else:
            post.likes_count += 1
            like = Like(user = request.user, post=post)
            like.save()
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=200)

class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
        
    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if post is None:
            return Response(status=404)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        user = request.user
        if post is None:
            return Response(status=404)
        data = {
            'user': user.id,
            'post': post.id,
            'body': request.data.get('body')
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            body = serializer.data['body']
            # print(body)
            post.comments_data = body
            post.save()
            return Response(status=201)
        return Response(status=400)