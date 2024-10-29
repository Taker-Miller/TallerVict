# Generated by Django 4.2.6 on 2024-10-29 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_venta_precio_unitario_alter_producto_stock_minimo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='precio_unitario',
        ),
        migrations.AlterField(
            model_name='venta',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
