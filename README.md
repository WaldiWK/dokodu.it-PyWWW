# Start

1. stwórz środowisko Python (patrz szkolenie PyWWW z serwisu dokodu.it)
`python3 -m venv pywww-venv`

2. stwórz wygodny link do aktywacji
`ln -s pywww-venv/bin/activate .`

3. uruchom środowisko
`source activate`

4. zainstaluj zależności
`pip install -r requirements.txt`

# szkolenie PyWWW z serwisu dokodu.it

`python3 -m venv nazwa_środowiska`
    tworzy środowisko o nazwie nazwa_środowiska

`source nazwa_środowiska/bin/activate`
    uruchamia stworzone środowisko 


`pip install nazwa_programu`
    instalacja programu pythona

`pip install Diango`
    instalacja Django

`pip freeze`
    wyświetlenie zależności zainstalowanych do tej pory w aktualnym środowisku

`pip freeze > requirements.txt`
    zapisanie powyższych zależności do pliku requirements.txt

`pip install -r requirements.txt`
    zainstalowanie zależności z pliku requirements.txt do aktywnego obecnie środowiska.

`deactivate` 
    wyłącza aktywne środowisko

`django-admin startproject nazwa` 
    tworzy projekt o nazwie nazwa

# Django shell

`python manage.py shell`
    Uruchamia zbootstrapowane Django w konsoli.
    Aby załądować modele itd, trzeba dodatkowo przeprowadzić import modelów.
        `from posts.models import Post`


# django-extensions
installacja:
`pip install django-extensions`

add to project:
`echo "# shell_plus" >>   pywww/settings.py`
`echo "SHELL_PLUS_PRINT_SQL = True" > settings.py`
