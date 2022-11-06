from django.urls import path
from .views import  articoloDetailView, NewsHome

urlpatterns=[ 
    path('',NewsHome,name="newshome"),
    path('articolo/<int:pk>', articoloDetailView, name="articolo_detail")
]