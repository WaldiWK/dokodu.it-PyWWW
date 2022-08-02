from django.urls import path
from . import views

urlpatterns = [
    path("1", views.post_details),
    path("", views.posts_list),
]