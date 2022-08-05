from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def posts_list(request):
    return render(request,"posts/list.html", context={
        "posts": Post.objects.all()
    })
    
def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,"posts/detail.html",context={
        "post": post
    })
    