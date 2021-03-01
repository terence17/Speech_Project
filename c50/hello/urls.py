from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.statement, name = "statement"),
    path("madridista", views.madridista, name="madridista"),
    path("jugadores", views.jugadores, name="jugadores")
]
