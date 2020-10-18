from django.shortcuts import render

from .models import Servicio

# Create your views here.


def servicios(request):

    servicios = Servicio.objects.all()  # importando absolutamente todo lo creado en la Clase Servicio de models

    return render(request, 'servicios_app/servicios.html', {"servicios": servicios})
