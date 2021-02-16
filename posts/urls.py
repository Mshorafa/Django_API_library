from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('api/postslist/', views.PostList.as_view(), name='api-posts-list'),
    path('api/<int:pk>/deleteposts/', views.DeletePost.as_view(), name='api-posts-delete'),
    path('api/createposts/', views.CreatePostList.as_view(), name='api-posts-create'),
    path('api/<int:pk>/createVote/', views.CreateVote.as_view(), name='api-vote-create'),
]
