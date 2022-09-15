from django.shortcuts import render
from django.template import loader, Context, Template
from django.http import HttpResponse
from AppMVT.models import Familia
#from django.template import Template, Context, Loader

# Create your views here.

def personas(self):

    diccionario = {"namePadre": "Carlos", "countryPadre": "Italia", "añosPadre": "46", "nameMadre": "Susana", "countryMadre": "Argentina", "añosMadre": "40", "nameHermano": "Pablo", "countryHermano": "Argentina", "añosHermano": "20"}
    #miHtml = open("C:/Users/a445831/OneDrive - Santander Office 365/Escritorio/Proyecto-web/MVT+Juan/MVT01/AppMVT/migrations/plantillas/plantillas1.html")
    #plantilla = loader.get_template("plantillas1.html")
    plantilla = loader.get_template("plantillas1.html")
    datos = plantilla.render(diccionario)
    return HttpResponse(datos)
