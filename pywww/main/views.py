from django.shortcuts import render


def about(request):
    return render (request,'main/about.html',context={})

def hello_world(request):
    return render (request,"main/hello_world.html",context={})   


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
