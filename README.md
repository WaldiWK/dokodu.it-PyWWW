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


# django-extensions
installacja:
    najpierw instalujemy django-extensions

`pip install django-extensions`

a następnie dodajemy 'django-extensions' do definicji aplikacji w settings.py, tuż przed modelami:
```python
...
# Application definition

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps fom external modules
    'django_extensions',
    # project apps
    'books.apps.BooksConfig',
    'posts.apps.PostsConfig',
]
...
```


Możemy wkleić też poniższe linie w terminala, dodadzą one odpowiednie wpisy do settings.py, aby shell_plus dodawał informacje o zapytaniach SQL:
```bash

echo "# shell_plus" >>   pywww/settings.py
echo "SHELL_PLUS_PRINT_SQL = True" > settings.pya
```
