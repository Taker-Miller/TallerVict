from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('jefe_dashboard/', views.jefe_dashboard, name='jefe_dashboard'),
    path('trabajador_dashboard/', views.trabajador_dashboard, name='trabajador_dashboard'),
    path('inventario/', views.inventario_view, name='inventario'),
    path('registro_ventas/', views.registro_ventas_view, name='registro_ventas'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),
     # Ruta para la vista de inventario del jefe
    path('inventario-jefe/', views.inventario_jefe_view, name='inventario_jefe'),

    # Ruta para agregar un producto
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    

    # Ruta para editar un producto existente
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('empleados/', views.gestion_empleados, name='gestion_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/lista/', views.lista_empleados, name='lista_empleados'),

    # Ruta para eliminar un producto existente
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    path('', views.login_view, name='home'),  # Cambia la ruta raíz a la página de login
    path('logout/', views.logout_view, name='logout'),  # Añadir la ruta de logout
    path('reportes/', views.generar_reportes_view, name='generar_reportes'),
]
