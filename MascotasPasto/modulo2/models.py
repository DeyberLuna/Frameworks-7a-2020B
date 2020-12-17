from django.db import models

# Create your models here.
class Afiliados(models.Model):
    id = models.IntegerField(default=0)
    nombres = models.CharField(max_lenght=100)
    apellidos = models.CharField(max_lenght=100)
    numero_movil = models.IntegerField(default=0)
    direccion = models.CharField(max_lenght=100)
    email = models.CharField(max_lenght=100)
    id_ciudad = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creation')
    fecha_modificacion = models.DateTimeField('Date update')

class Paises(models.Model) :
    id = models.IntegerField(default=0)
    codigo = models.CharField(max_lenght=50)
    nombre = models.CharField(max_lenght=100)
    abreviatura = models.CharField(max_lenght=20)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creation')
    fecha_modificacion = models.DateTimeField('Date update')

class Ciudades(models.Model) :
    id = models.IntegerField(default=0)
    codigo = models.CharField(max_lenght=50)
    nombre = models.CharField(max_lenght=100)
    abreviatura = models.CharField(max_lenght=20)
    id_pais = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField('Date creation')
    fecha_modificacion = models.DateTimeField('Date update')