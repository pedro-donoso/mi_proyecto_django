from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm, RegistroForm

@login_required(login_url='login')
def lista_libros(request):
    libros = Libro.objects.all()
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'catalogo/lista_libros.html', {'libros': libros, 'form': form})

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
        
    else:
        form = RegistroForm()
    return render(request, 'catalogo/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')
        
    else:
        form = AuthenticationForm()
    return render(request, 'catalogo/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')