from django.contrib import admin
from .models import Producto, Lista
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    
    fields = ['nombre', 'descripcion']

admin.site.register(Producto, ProductoAdmin)
