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
    stock_minimo = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)  # Campo para la imagen

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateField()  # Este campo debe ser proporcionado en el formulario
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad} unidades'

class Empleado(models.Model):
    ROL_CHOICES = [
        ('jefe', 'Jefe'),
        ('trabajador', 'Trabajador'),
    ]
    
    nombre = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, choices=ROL_CHOICES)  # Campo de selección
    email = models.EmailField(unique=True, default='placeholder@example.com')  
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.get_rol_display()})"
