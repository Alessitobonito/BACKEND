from django.db import models
from datetime import datetime

class Producto(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    descripcion = models.TextField(null=True)
    class Meta:
        db_table = 'productos'

class Lista(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombrePropietario = models.TextField(
        db_column='nombre_propietario', null=False)
    fechaCreacion = models.DateTimeField(
        db_column='fecha_creacion', null=False, default=datetime.now)
    class Meta:
        db_table = 'listas'