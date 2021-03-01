from django.shortcuts import render
from django.urls import reverse
from .models import Speech
from .models import Speaker


from speeches.models import Speech




# Create your views here.
def index(request):

    return render(request, "speeches/index.html")

def speech(request):
    context = {
        "speak" : Speech.objects.all()
    } 
    return render(request, "Speeches/speech.html", context) 

def speakers(request):
    context = {
        "speaker" : Speaker.objects.all()
    }
    return render(request, "Speeches/speakers.html", context)     



  
         