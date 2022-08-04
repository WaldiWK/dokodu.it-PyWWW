from django.shortcuts import render
from .models import Book

def books_list(request):
    context = {
        "title":"Mój spis książek",
        "books": Book.objects.all()
    }
    return render(request,"books/books_list.html",context)
    
