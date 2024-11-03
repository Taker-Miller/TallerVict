from django import forms
from .models import Producto, Venta, Empleado

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'stock_minimo', 'imagen']
        labels = {
            'nombre': 'Nombre del Producto',
            'precio': 'Precio',
            'stock': 'Stock Disponible',
            'stock_minimo': 'Stock Mínimo',
            'imagen': 'Imagen del Producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el nombre del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el precio',
                'step': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad en stock'
            }),
            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el stock mínimo'
            }),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        return stock

    def clean_stock_minimo(self):
        stock_minimo = self.cleaned_data.get('stock_minimo')
        if stock_minimo < 0:
            raise forms.ValidationError('El stock mínimo no puede ser negativo.')
        return stock_minimo
    

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad', 'fecha']  # Asegúrate de incluir el campo 'fecha'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})  # Asegúrate de que sea un input de tipo date
        }



class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'rol', 'codigo', 'imagen']

    def clean(self):
        cleaned_data = super().clean()
        rol = cleaned_data.get("rol")
        codigo = cleaned_data.get("codigo")
        
        # Validar que el código solo sea obligatorio si el rol es "Jefe"
        if rol == "Jefe" and not codigo:
            self.add_error("codigo", "El código es obligatorio para el rol de Jefe.")
        elif rol == "Jefe" and codigo != "123":
            self.add_error("codigo", "Código incorrecto para el rol de Jefe.")
        elif rol != "Jefe":
            # Si no es jefe, asegúrate de que el campo código esté vacío
            cleaned_data["codigo"] = None

        return cleaned_data




