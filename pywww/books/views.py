from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_library(request):
    return HttpResponse('Tu Będzie moja Biblioteka')
    