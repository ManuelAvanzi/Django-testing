from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def LibreriaHome(request):
    return HttpResponse("<h1>Questa è la Homepage della applicazione Libreria</h1>")

def LibreriaBlog(request):
    return HttpResponse("<h1>Questa è la pagina della libreria dedicata al blog</h1>")

def LibreriaContatti(request):
    return HttpResponse("<h1>QUesta è la pagina dei contatti</h1>")