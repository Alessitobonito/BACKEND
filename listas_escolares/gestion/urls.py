from django.urls import path
from .views import paginaInicial

urlpatterns = [
    path('inicio', paginaInicial),
]