from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.lista_libros, name='lista_libros'),
]
