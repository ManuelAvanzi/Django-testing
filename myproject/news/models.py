from django.db import models
from django.urls import reverse

# Create your models here.

class Giornalista(models.Model):
    nome=models.CharField(max_length=30)
    cognome=models.CharField(max_length=40)

    def __str__(self):
        return self.nome+" "+self.cognome


class Articolo(models.Model):
    titolo=models.CharField(max_length=40)
    contenuto=models.TextField()
    giornalista=models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse ("articolo_detail",kwargs={"pk":self.pk})