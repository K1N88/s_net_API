from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Post, Group
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer
from api.permissions import AuthorPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, AuthorPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, AuthorPermission]

    def get_post(self):
        return get_object_or_404(
            Post,
            id=self.kwargs.get("post_id")
        )

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.get_post().id
        )
