from django.urls import path 

from . import views


app_name = "speeches"
urlpatterns = [
    path("", views.index, name="index"),
    path("speech", views.speech, name="speech"),
    path("speakers", views.speakers, name="speakers")
]