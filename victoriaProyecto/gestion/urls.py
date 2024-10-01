from django.urls import path
from . import views

urlpatterns = [
    # Rutas de Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    # Inventario
    path('inventario/', views.inventario_view, name='inventario'),
    path('inventario-jefe/', views.inventario_jefe_view, name='inventario_jefe'),

    # Registro de Ventas
    path('registro_ventas/', views.registro_ventas_view, name='registro_ventas'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),

    # Reportes
    path('reportes/', views.generar_reportes_view, name='generar_reportes'),

    # Gestión de Empleados
    path('empleados/', views.gestion_empleados, name='gestion_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/lista/', views.lista_empleados, name='lista_empleados'),
    
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/<int:pk>/editar/', views.editar_empleado, name='editar_empleado'),
    path('empleados/<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
]
