# Generated by Django 5.1.2 on 2024-10-28 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_product_imagen_product_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('cantidad', models.IntegerField()),
                ('precio_parcial', models.IntegerField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado')], max_length=10)),
                ('correo', models.EmailField(max_length=128)),
            ],
        ),
    ]