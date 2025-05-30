from forum_app.models import Post, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny



# defines a view for listing and creating posts.
class PostListCreateView(generics.ListCreateAPIView):

    # retrieves all Post objects from the database.
    queryset = Post.objects.all()

    # specifies the serializer to format Post objects.
    serializer_class = PostSerializer

    # applies the custom permission class.
    permission_classes = [IsOwnerOrReadOnly]

    # customizes the creation of new Post objects.
    def perform_create(self, serializer):

        # sets the authenticated user as the author of the post.
        serializer.save(author=self.request.user)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)


# defines a view for retrieving, updating, and deleting a single post.
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):

    # retrieves all Post objects from the database.
    queryset = Post.objects.all()

    # specifies the serializer to format Post objects.
    serializer_class = PostSerializer

    # applies the custom permission class to control access.
    permission_classes = [IsOwnerOrReadOnly]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]