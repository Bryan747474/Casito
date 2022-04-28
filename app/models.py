from django.db import models

# Create your models here.

# 2 entidades con sus atributos


class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def _str_(self):
        return self.tipo


class TipoMascota(models.Model):
    tipo = models.CharField(max_length=20)

    def _str_(self):
        return self.tipo



class TipoCliente(models.Model):
    tipo = models.CharField(max_length=20)

    def _str_(self):
        return self.tipo





class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto,on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre



class Mascota(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    años = models.IntegerField()
    tipo = models.ForeignKey(TipoMascota,on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre




class Cliente(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=20)
    mail = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoCliente,on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre


    # python manage.py makemigration crea el script dela base de datos

    # python manage.py migrate crea la base de datos a partir del script


    # admin ---- admin1