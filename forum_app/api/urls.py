from django.urls import path
from .views import PostListCreateView, CommentListCreateView, PostDetailView, CommentDetailView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('comments/', CommentListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('comments/<int:pk>/', CommentDetailView.as_view()),
]
