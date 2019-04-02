from django.urls import path
from django.conf.urls import url
from post.views import *

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('posts/', posts, name='posts'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('post_create_view/', post_create_view, name = 'post_create_view'),
    path('posts/<int:id>/delete/', post_delete ,name = 'delete'),
    path('posts/<int:id>/update/', post_update, name = 'update'),
]