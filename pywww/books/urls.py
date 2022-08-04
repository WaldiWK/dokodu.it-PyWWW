from django.urls import path
from . import views

urlpatterns = [
    # path("/details", views.book_details),
    path("", views.books_list),
]
