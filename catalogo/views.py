from django.shortcuts import render, redirect

from .models import Libro

from .forms import LibroForm

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
