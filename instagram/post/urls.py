from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_pk>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/', views.post_detail, name='post_detail'),
]
