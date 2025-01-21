
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer

def mostrarProductosPlantilla(request):
    data = Producto.objects.all()
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje':'Bienvenido'})

def crearProductoFormulario(request):
    if request.method == 'POST':
        nombreProducto = request.POST.get('nombreProducto')
        descripcionProducto = request.POST.get('descripcionProducto')
        nuevoProducto = Producto(nombre=nombreProducto, descripcion=descripcionProducto)
        nuevoProducto.save()
        return redirect('mostrar_productos')
    return render(request, 'formulario_producto.html')

def editarProductoFormulario(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombreProducto')
        producto.descripcion = request.POST.get('descripcionProducto')
        producto.save()
        return redirect('mostrar_productos')
    return render(request, 'formulario_producto.html', {'producto': producto})

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('mostrar_productos')


@api_view(['GET', 'POST'])
def validarFuncionamiento(request):
    if request.method == 'GET':
        return Response(data={
            'message': 'El servidor está funcionando correctamente'
        })
    
    elif request.method == 'POST':
        return Response(data={
            'message': 'Informacion aceptada correctamente'
        })

class ProductosController(GenericAPIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializador = ProductoSerializer(Producto.objects.all(), many=True)
        serializador.data
        
        return Response(data={
            'message': 'Los productos son',
            'content': serializador.data
        })
    
    def post(self, request):
        data = request.data
        serializador = ProductoSerializer(data=data)

        if serializador.is_valid():
            serializador.save()
            return Response(data={
            'message': 'Producto creado correctamente'
        })
        else:
            return Response(data={
                'message': 'error al crear el producto',
                'content': serializador.errors
            })
class ListarYCrearProductosController(ListCreateAPIView):
    # Para utilizar una vista generica se tiene que definir los siguientes atributos
    # Como obtendra la informacion y la devolvera
    queryset = Producto.objects
    # Para indicar como tiene que validar y devolver la informacion proveniente de la bd
    serializer_class = ProductoSerializer


class DevolverActualizarEliminarProductoController(RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects
    serializer_class = ProductoSerializer
    # Si cambiamos el nombre del parametro en nuestra url
    lookup_field = 'id'