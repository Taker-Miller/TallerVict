from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Login y Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Ruta de logout

    # Dashboards
    path('jefe_dashboard/', views.jefe_dashboard, name='jefe_dashboard'),
    path('trabajador_dashboard/', views.trabajador_dashboard, name='trabajador_dashboard'),

    # Inventario
    path('inventario/', views.inventario_view, name='inventario'),
    path('inventario-jefe/', views.inventario_jefe_view, name='inventario_jefe'),

    # Productos
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    path('anadir_venta/', views.anadir_venta, name='anadir_venta'),
    path('registro_ventas/', views.registro_ventas, name='registro_ventas'),
    path('productos/', views.lista_productos, name='lista_productos'),


    # Registro de ventas
    path('registro_ventas/', views.registro_ventas_view, name='registro_ventas'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),

    # Reportes
    path('reportes/', views.generar_reportes_view, name='generar_reportes'),

    # Gestión de empleados
    path('empleados/', views.lista_empleados, name='lista_empleados'),  # Ruta para la lista de empleados
    path('empleados/gestion/', views.lista_empleados, name='gestion_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),  # Ruta para agregar empleado
    path('empleados/<int:pk>/editar/', views.editar_empleado, name='editar_empleado'),
    path('empleados/<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),

    # Redirigir la raíz al login
    path('', views.login_view, name='home'),
]
