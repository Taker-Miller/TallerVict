from django.contrib import admin
from .models import Producto, Venta, Empleado

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Empleado)
