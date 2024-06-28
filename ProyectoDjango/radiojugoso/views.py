from django.shortcuts import render


def index(request):
    return render(request, 'radiojugoso/index.html')

def noticias(request):
    return render(request, 'radiojugoso/noticias.html')

def galeria(request):
    return render(request, 'radiojugoso/galeria.html')

def tienda(request):
    return render(request, 'radiojugoso/tienda.html')

def contacto(request):
    return render(request, 'radiojugoso/contacto.html')