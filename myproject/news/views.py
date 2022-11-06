from django.shortcuts import render
from django.http import HttpResponse

from .models import Articolo,Giornalista
# Create your views here.

# def NewsHome(request):
#     return HttpResponse("<h1>Home page della applicazione News")

def NewsHome(request):
    
    a=[]
    g=[]

    for art in Articolo.objects.all():
        a.append(art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g.append(gio.nome+" "+gio.cognome +"<br>")

    response=str(a)+"<br>"+"<h1>Giornalisti</h1>"+str(g)
    return HttpResponse("<h1>Articoli</h1> <br> <h3>"+ response+ "</h3>")