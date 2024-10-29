from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.utils.dateparse import parse_date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ProductoForm, VentaForm
from .models import Producto
from .forms import ProductoForm
from .models import Empleado, Producto, Venta 

# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == 'jefe':  # Detecta si el usuario es el jefe
                request.session['role'] = 'jefe'
                return redirect('jefe_dashboard')  # Redirige al dashboard del jefe
            elif user.username == 'trabajador':
                request.session['role'] = 'trabajador'
                return redirect('trabajador_dashboard')  # Redirige al dashboard del trabajador
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'gestion/login.html')



# Vista para el dashboard del jefe
def jefe_dashboard(request):
    if request.session.get('role') == 'jefe':
        return render(request, 'gestion/jefe_dashboard.html')  # Cargar la plantilla jefe_dashboard.html
    else:
        return redirect('login')  # Si no es jefe, redirigir al login

def inventario_jefe_view(request):
    productos = Producto.objects.all()  # Obtenemos todos los productos
    return render(request, 'gestion/inventario_jefe.html', {'productos': productos})




# Vista para añadir un producto
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto añadido con éxito.')
            return redirect('inventario_jefe')  # Redirige al inventario después de añadir un producto
    else:
        form = ProductoForm()

    return render(request, 'gestion/agregar_producto.html', {'form': form})


# Vista para editar un producto existente

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # Mostrar mensaje de éxito con el stock restante
            messages.success(request, f'El producto "{producto.nombre}" ha sido actualizado. Stock restante: {producto.stock}')
            
            # Comprobar si el stock está por debajo del stock mínimo
            if producto.stock <= producto.stock_minimo:
                messages.warning(request, f'¡Atención! El stock del producto "{producto.nombre}" está por debajo del nivel mínimo ({producto.stock_minimo}).')
            
            return redirect('inventario_jefe')  # Redirige al inventario del jefe
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'gestion/editar_producto.html', {'form': form, 'producto': producto})


# Vista para eliminar un producto
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado con éxito.')
        return redirect('inventario_jefe')
    return render(request, 'gestion/eliminar_producto.html', {'producto': producto})

def generar_reportes_view(request):
    ventas = []
    total_ventas = 0

    if request.method == 'POST':
        fecha_desde = request.POST.get('fecha_desde')
        fecha_hasta = request.POST.get('fecha_hasta')

        if fecha_desde and fecha_hasta:
            # Convertir las fechas a objetos de fecha de Django
            fecha_desde = parse_date(fecha_desde)
            fecha_hasta = parse_date(fecha_hasta)

            # Filtrar ventas entre las fechas seleccionadas
            ventas = Venta.objects.filter(fecha__range=[fecha_desde, fecha_hasta])
            total_ventas = sum(venta.total for venta in ventas)
        else:
            messages.error(request, "Por favor selecciona ambas fechas")

    return render(request, 'gestion/reportes.html', {
        'ventas': ventas,
        'total_ventas': total_ventas,
    })


# Vista para la lista de empleados
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestion/lista_empleados.html', {'empleados': empleados})

# Vista para agregar un empleado (esto lo usaremos más adelante)
def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        rol = request.POST.get('rol')
        Empleado.objects.create(nombre=nombre, rol=rol)
        return redirect('lista_empleados')
    return render(request, 'gestion/agregar_empleado.html')

# Vista para editar un empleado (esto lo usaremos más adelante)
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.rol = request.POST.get('rol')
        empleado.save()
        return redirect('lista_empleados')
    return render(request, 'gestion/editar_empleado.html', {'empleado': empleado})

# Vista para eliminar un empleado
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'gestion/eliminar_empleado.html', {'empleado': empleado})


def gestion_empleados(request):
    return render(request, 'gestion/gestion_empleados.html')



def agregar_empleado(request):
    # Lógica para agregar empleado
    return render(request, 'gestion/agregar_empleado.html')

def lista_empleados(request):
    # Lógica para mostrar la lista de empleados
    return render(request, 'gestion/lista_empleados.html')


# Vista para el dashboard del trabajador
def trabajador_dashboard(request):
    if request.session.get('role') == 'trabajador':
        return render(request, 'gestion/trabajador_dashboard.html')  # Cargar template trabajador_dashboard.html
    else:
        return redirect('login')



productos = [
    {'nombre': 'Collar', 'precio': 5500, 'stock': 3},
    {'nombre': 'Pulsera Plata', 'precio': 10000, 'stock': 2},
]

def inventario_view(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda
    if query:
        # Filtrar productos que contengan el término de búsqueda
        productos_filtrados = [producto for producto in productos if query.lower() in producto['nombre'].lower()]
    else:
        productos_filtrados = productos  # Mostrar todos los productos si no hay búsqueda

    return render(request, 'gestion/inventario.html', {'productos': productos_filtrados})


def registro_ventas_view(request):
    # Obtener todas las ventas y productos de la base de datos
    ventas = Venta.objects.all().order_by('fecha')
    productos = Producto.objects.all()  # Obtener todos los productos de la base de datos

    # Calcular el total del día
    total_dia = sum(venta.total for venta in ventas)

    # Agrupar ventas por fecha
    ventas_por_fecha = {}
    for venta in ventas:
        if venta.fecha not in ventas_por_fecha:
            ventas_por_fecha[venta.fecha] = []
        ventas_por_fecha[venta.fecha].append(venta)

    if request.method == 'POST':
        # Buscar producto y registrar una nueva venta
        producto_buscado = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 0))

        try:
            producto = Producto.objects.get(nombre=producto_buscado)  # Busca el producto por nombre
            subtotal = producto.precio * cantidad
            
            # Crear y guardar la venta
            venta = Venta.objects.create(producto=producto, cantidad=cantidad, fecha=request.POST.get('fecha_venta'))
            venta.total = subtotal  # Asignar el subtotal al total de la venta
            venta.save()

            messages.success(request, 'Venta registrada con éxito')
        except Producto.DoesNotExist:
            messages.error(request, "Producto no encontrado")

    return render(request, 'gestion/registro_ventas.html', {
        'ventas_por_fecha': ventas_por_fecha,
        'total_dia': total_dia,
        'productos': productos,
    })




def registro_ventas(request):
    ventas = Venta.objects.all().order_by('fecha')
    ventas_por_fecha = {}
    
    for venta in ventas:
        if venta.fecha not in ventas_por_fecha:
            ventas_por_fecha[venta.fecha] = []
        ventas_por_fecha[venta.fecha].append(venta)

    # Calculate total sales for each date
    total_por_fecha = {fecha: sum(venta.total for venta in ventas) for fecha, ventas in ventas_por_fecha.items()}

    context = {
        'ventas_por_fecha': ventas_por_fecha,
        'total_por_fecha': total_por_fecha,  # Pass the total per date
        'total_dia': sum(venta.total for venta in ventas)  # Total of all sales
    }

    return render(request, 'gestion/registro_ventas.html', context)





# Otra vista para procesar la venta
def registrar_venta(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        cantidad = int(request.POST.get('cantidad', 0))
        fecha = request.POST.get('fecha')

        try:
            producto = Producto.objects.get(id=producto_id)
            if cantidad > producto.stock:
                messages.error(request, "No hay suficiente stock disponible.")
                return redirect('anadir_venta')

            total = producto.precio * cantidad
            venta = Venta.objects.create(producto=producto, cantidad=cantidad, fecha=fecha, total=total)

            # Restar el stock
            producto.stock -= cantidad
            producto.save()

            messages.success(request, 'Venta registrada con éxito.')
            return redirect('registro_ventas')

        except Producto.DoesNotExist:
            messages.error(request, "Producto no encontrado.")
            return redirect('anadir_venta')

    return redirect('anadir_venta')






def anadir_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)  # No guardar aún en la base de datos
            producto = venta.producto

            # Verificar si hay suficiente stock
            if producto.stock >= venta.cantidad:
                # Restar el stock
                producto.stock -= venta.cantidad
                producto.save()  # Guardar los cambios en el stock

                # Guardar la venta
                venta.save()

                # Mostrar mensaje de éxito
                messages.success(request, 'La venta ha sido registrada exitosamente.')
                
                # Redirigir al registro de ventas
                return redirect('registro_ventas')
            else:
                messages.error(request, 'No hay suficiente stock para realizar la venta.')
        else:
            messages.error(request, 'Hubo un error con la venta. Verifica los datos ingresados.')
    else:
        form = VentaForm()

    productos = Producto.objects.all()  # Obtener todos los productos disponibles para el select
    return render(request, 'gestion/anadir_venta.html', {'form': form, 'productos': productos})

def lista_productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'gestion/lista_productos.html', {'productos': productos})



# Vista de logout (cerrar sesión)
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login después de cerrar sesión



def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':  # Si se confirma la eliminación
        producto.delete()
        messages.success(request, f'Producto "{producto.nombre}" eliminado con éxito.')
        return redirect('inventario_jefe')  # Redirigir al inventario del jefe después de eliminar
    
    return render(request, 'gestion/eliminar_producto.html', {'producto': producto})

