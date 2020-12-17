from django.db import models

# Create your models here.
# Modelo categoria
class Category(models.Model) :
    code = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_date = models.DateTimeField('Date creation')
    update_date = models.DateTimeField('Date update')

    def __str__(self):
        return self.name, self.code

class Vendor(models.Model) :
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

class Client(models.Model) :
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
   