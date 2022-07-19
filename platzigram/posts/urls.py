from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.PostsListView.as_view(), name='list_posts'),
    path('posts/detail', views.PostDetailView.as_view(), name='detail_post'),
    path('posts/new', views.create_post, name='create_post'),
]
