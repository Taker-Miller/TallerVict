from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestion import views

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Login y Logout
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards
    path('jefe_dashboard/', views.jefe_dashboard, name='jefe_dashboard'),
    path('trabajador_dashboard/', views.trabajador_dashboard, name='trabajador_dashboard'),

    # Inventario
    path('inventario/', views.inventario_view, name='inventario'),
    path('inventario-jefe/', views.inventario_jefe_view, name='inventario_jefe'),

    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
    
    # Venta
    path('anadir_venta/', views.anadir_venta, name='anadir_venta'),
    path('registro_ventas/', views.registro_ventas, name='registro_ventas'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),

    # Registro de Ventas para el Jefe
    path('ventas_jefe/', views.registro_ventas_jefe_view, name='ventas_jefe'),

    # Reportes
    path('reportes/', views.generar_reportes_view, name='generar_reportes'),

    # Gestión de Empleados
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/gestion/', views.gestion_empleados, name='gestion_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/<int:pk>/editar/', views.editar_empleado, name='editar_empleado'),
    path('empleados/<int:pk>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),

    # Redirigir la raíz al login
    path('', views.login_view, name='home'),
]

# Configuración para servir archivos de medios en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
