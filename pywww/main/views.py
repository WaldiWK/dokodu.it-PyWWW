#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def hello_world(request):
    template = loader.get_template('main/about.html')
    return HttpResponse(template.render())


def some_tests(request):
    age = 33
    first_name = 'Kacper'
    children = ['Aniela', 'Rozalia', 'Julian']
    programming_languages = {
        'python': 'advanced',
        'php': 'advanced',
        'js': 'intermediate'
    }
    books = set(['czysty kod', "PostgreSQL Biblia", "Efektywny Python"])
    return render(request, "main/some_tests.html", context={
        "age": age,
        "first_name": first_name,
        "children": children,
        "languages": programming_languages,
        "books": books,
    })
