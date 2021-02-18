from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from . import serializers, models


# Create your views here.


class PostList(generics.ListAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostsSerialzier


class CreatePostList(generics.ListCreateAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostsSerialzier
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class CreateVote(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = serializers.voteSerialzier
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post_id = models.Posts.objects.get(pk=self.kwargs['pk'])
        return models.Votes.objects.filter(voter=user, post=post_id)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('Your are all ready voted ')
        serializer.save(voter=self.request.user,
                        post=models.Posts.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never Voted on this post....silly!')


class DeletePost(generics.RetrieveDestroyAPIView):
    queryset = models.Posts.objects.all()
    serializer_class = serializers.PostsSerialzier
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = models.Posts.objects.filter(
            pk=self.kwargs['pk'], poster=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This is not your post :( !')
