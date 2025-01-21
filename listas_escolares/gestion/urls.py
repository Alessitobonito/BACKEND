from django.urls import path
from .views import *

urlpatterns = [
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductoFormulario, name='crear_producto'),
]