from django.shortcuts import render, redirect
from .models import Producto

def mostrarProductosPlantilla(request):

    print(request)

    data = Producto.objects.all()
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje':'Bienvenido'})

def crearProductoFormulario(request):
    if request.method == 'POST':
        print(request.POST)
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        nuevoProducto = Producto(nombre = nombreProducto, descripcion = descripcionProducto)
        nuevoProducto.save()
        return redirect('mostrar_productos')
    elif request.method == 'GET':
         print('queremos ver el formulario')
    return render(request, 'formulario_producto.html')