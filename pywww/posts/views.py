from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def posts_list(request):
    return HttpResponse(Post.objects.all())
    
def first_post(request):
    post = Post.objects.first()
    html=f"<h2> {post.title} </h2>"
    html += f''' <div>
            <small>Utworzono {post.created}, zmodyfikowano {post.modified} </small>
        </div>
        <div>
            <p> {post.content} </p>
        </div>
    '''
    return HttpResponse(html)