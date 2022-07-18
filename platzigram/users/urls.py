# Django
from django.urls import path
# Views
from django.views.generic import TemplateView
from . import views

app_name = "users"

urlpatterns = [
    # Posts
    path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail.html'),
        name='detail'
    ),

    # User management
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    path('me/profile/', views.update_profile, name='update_profile'),
]
