from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):

    return render(request, 'gestion_pedidos_app/home.html')


def tienda(request):

    return render(request, 'gestion_pedidos_app/tienda.html')


def contacto(request):

    return render(request, 'gestion_pedidos_app/contacto.html')
