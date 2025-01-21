from django.shortcuts import render, redirect

def mostrarProductosPlantilla(request):

    print(request)
    data = [
        {
        'id': 1,
        'nombre': 'Lapiz Faber Castell',
        'descripcion': 'Lapiz B2'
        },
        {
            'id': 2,
            'nombre': 'Resaltador color amarillo',
            'descripcion': None
        }
    ]
    return render(request, 'mostrar_productos.html', {'data': data, 'mensaje':'Bienvenido'})

def crearProductoFormulario(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('mostrar_productos')
    elif request.method == 'GET':
         print('queremos ver el formulario')
    return render(request, 'formulario_producto.html')