from django.urls import path
from .views import LibreriaBlog,LibreriaContatti,LibreriaHome

urlpatterns=[
    path('',LibreriaHome,name="libreriaHome"),
    path('contatti',LibreriaContatti,name="contatti"),
    path('blog',LibreriaBlog,name="blog")
]