from django.db import models

# Create your models here.
class Mascotas(models.Model) :
    id= models.IntegerField()
    codigo= models.IntegerField()
    id_tipo= models.IntegerField()
    id_raza= models.IntegerField()
    nombre= models.CharField(max_lenght=100)
    tiene_vacunas= models.BooleanField(default=True)
    estado= models.BooleanField(default=True)
    fecha_creacion= models.DateTimeField('Date creation')
    fecha_modificacion= models.DateTimeField('Date update')

    

class Tipos(models.Model) :
    id= models.IntegerField()
    codigo= models.CharField(max_lenght=50)
    nombre= models.CharField(max_lenght=100)
    abreviatura= models.CharField(max_lenght=20)
    estado= models.BooleanField(default=True)
    fecha_creacion= models.DateTimeField('Date creation')
    fecha_modificacion= models.DateTimeField('Date update')

class Razas(models.Model) :
    id= models.IntegerField()
    codigo= models.CharField(max_lenght=50)
    nombre= models.CharField(max_lenght=100)
    abreviatura= models.CharField(max_lenght=20)
    id_pais= models.IntegerField(max_length=30)
    estado= models.BooleanField(default=True)
    fecha_creacion= models.DateTimeField('Date creation')
    fecha_modificacion= models.DateTimeField('Date update')
