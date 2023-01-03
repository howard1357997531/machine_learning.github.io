from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("a1/", views.a1, name='a1'),
    path("a2/", views.a2, name='a2'),
    path("a3/", views.a3, name='a3'),
    path("a4/", views.a4, name='a4'),
    path("a5/", views.a5, name='a5'),
    path("a6/", views.a6, name='a6'),
    path("a7/", views.a7, name='a7'),
    path("a8/", views.a8, name='a8'),
]
