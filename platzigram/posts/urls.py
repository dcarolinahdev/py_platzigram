from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('posts/new', views.create_post, name='create_post'),
]
