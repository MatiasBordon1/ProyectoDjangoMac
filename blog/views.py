from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post_list})