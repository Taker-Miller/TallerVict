from django import forms
from .models import Producto  # Importamos el modelo Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock']  # Ajusta los campos según tu modelo Producto

        # Definimos etiquetas para que se muestren en el formulario
        labels = {
            'nombre': 'Nombre del Producto',
            'precio': 'Precio',
            'stock': 'Stock Disponible',
        }

        # Definimos los widgets (apariencia de los campos) para dar estilos y personalizar los inputs
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el nombre del producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduce el precio',
                'step': '0.01'  # Para manejar decimales en el precio
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad en stock'
            }),
        }

    # Validación personalizada de los datos
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
