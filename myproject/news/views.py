from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Articolo,Giornalista
# Create your views here.

# def NewsHome(request):
#     return HttpResponse("<h1>Home page della applicazione News")

# def NewsHome(request):
    
#     a=[]
#     g=[]

#     for art in Articolo.objects.all():
#         a.append(art.titolo + "<br>")

#     for gio in Giornalista.objects.all():
#         g.append(gio.nome+" "+gio.cognome +"<br>")

#     response=str(a)+"<br>"+"<h1>Giornalisti</h1>"+str(g)
#     return HttpResponse("<h1>Articoli</h1> <br> <h3>"+ response+ "</h3>")

def NewsHome(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={"articoli":articoli,"giornalisti":giornalisti}
    return render(request,"newshomepage.html",context)

def articoloDetailView(request,pk):
    # articolo=Articolo.objects.get(pk=pk)
    articolo=get_object_or_404(Articolo,pk=pk)
    context={"articolo":articolo}
    return render(request,"articolo_detail.html",context)

    