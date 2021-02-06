from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=10)

    def __str__(self):
        return """El nobre es %s, la direccion es %s,
        el tel es %s y el email es %s""" % (
            self.nombre, self.direccion, self.tel, self.email
        )


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return "El nombre es %s, la seccion es %s, y el precio es %s" % (
            self.nombre, self.seccion, self.precio
        )


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return "El numero es %s, la fecha es %s, y su entrega fue %s" % (
            self.numero, self.fecha, self.entregado
        )