from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    # post
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_pk>/', views.post_detail, name='post_detail'),
    path('<int:post_pk>/like-toggle/', views.post_like_toggle, name='post_like_toggle'),

    # Comment
    path('<int:post_pk>/comment/create/', views.comment_create, name='comment_create'),
]
