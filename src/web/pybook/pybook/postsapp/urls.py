
from django.urls import path

from . import views

app_name = 'postsapp'
urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
    path('posts', views.new_post, name='new_post'),
    ]
