from django.urls import path
from apps.posts.views import *

app_name = 'posts'

urlpatterns = [
    path('', ListPostView.as_view(), name='feed'),
    path('posts/new', CreatePostView.as_view(), name='create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('likes', likes_posts, name='likes')
]