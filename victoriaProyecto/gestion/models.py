from django.db import models
from django.contrib.auth.models import User

class Jefe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Trabajador(models.Model):
    jefe = models.ForeignKey(Jefe, on_delete=models.CASCADE, related_name='trabajadores')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre}"




class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)  # Por ejemplo: Jefe, Empleado, etc.

    def __str__(self):
        return self.nombre
