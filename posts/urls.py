from django.urls import path
from .views import (
    UserPostAPIView,
    PostSearchAPIView,
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView, 
    PostUpdateAPIView, 
    PostDeleteAPIView,
    LikeAPIView,
    CommentAPIView
) 

urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('search/', PostSearchAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
    path('<int:pk>/', PostDetailAPIView.as_view()),
    path('<int:pk>/update/', PostUpdateAPIView.as_view()),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view()),
    path('<int:pk>/like/', LikeAPIView.as_view()),
    path('<int:pk>/comment/', CommentAPIView.as_view()),
    path('<username>/', UserPostAPIView.as_view())
]