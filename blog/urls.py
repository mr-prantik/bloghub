from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
    path("author/<str:author_name>", views.author, name="blog-author")
]
