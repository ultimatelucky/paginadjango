from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return redirect('index')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Cuenta creada para {user.username}')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'radiojugoso/register.html', {'form': form})