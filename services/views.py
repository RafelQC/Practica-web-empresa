from django.shortcuts import render
#importam els serveis del model Services per a poder importar les bases de dades amb els serveis guardats
from .models import Services

# Create your views here.

def services(request):
    #pasam totes les dades del model Services
    service = Services.objects.all()
    #quan ens fan un request de la pagina, també incluim un diccionari amb tot el contingut dels serveis
    return render(request,"services/services.html", {'service':service})