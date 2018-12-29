from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'post/post_list.html', context)
