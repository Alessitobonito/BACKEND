from django.urls import path
from .views import (mostrarProductosPlantilla,
                    crearProductoFormulario,
                    editarProductoFormulario,
                    eliminarProducto,
                    validarFuncionamiento,
                    ProductosController,
                    ListarYCrearProductosController,
                    DevolverActualizarEliminarProductoController)

urlpatterns = [
    path('mostrar-productos', mostrarProductosPlantilla, name='mostrar_productos'),
    path('crear-producto', crearProductoFormulario, name='crear_producto'),
    path('editar-producto/<int:id>', editarProductoFormulario, name='editar_producto'),
    path('eliminar-producto/<int:id>', eliminarProducto, name='eliminar_producto'),
    path('validar-funcionamiento', validarFuncionamiento),
    path('productos', ProductosController.as_view()),
    path('productos-v2',ListarYCrearProductosController.as_view()),
    # Cuando usamos alguna de las vistas genericas que devuelvan, actualicen o eliminen un registro en la ruta tenemos que agregar el `pk`
    # Solamente aceptara el pk, si colocamos otro nombre, lanzara un error y por ende no podremos realizar la accion
    # Si queremos cambiar el nombre debemos establecerlo en el atributo lookup_field
    path('producto/<id>', DevolverActualizarEliminarProductoController.as_view())
]
