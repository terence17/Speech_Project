from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def madridista(request):
    return HttpResponse("Hola Camaradas, hoy tenemos una batalla. Vamos Real, Luchando juntos ")   

def jugadores(request):
    return HttpResponse("estamos aqui para luchar por ti")     

def statement(request, name):
    return render(request, "hello/statement.html",{
        "name": name.capitalize()
    })