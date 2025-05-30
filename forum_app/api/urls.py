from django.urls import path
from .views import PostListCreateView, CommentListCreateView, PostDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('posts/', PostDetailView.as_view()),
]
