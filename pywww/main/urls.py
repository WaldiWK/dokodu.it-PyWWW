from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.about, name="about"),
    path('testy', views.some_tests, name="some_tests"),
    path('hello_world', views.hello_world, name="hello_world")
]
