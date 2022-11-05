from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Questa è la mia Homepage </h1>")
