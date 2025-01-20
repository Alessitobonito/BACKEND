from django.shortcuts import render

def paginaInicial(request):

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
    return render(request, 'inicio.html', {'data': data, 'mensaje':'Bienvenido'})