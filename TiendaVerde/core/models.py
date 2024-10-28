from django.db import models

# Create your models here.
class Product (models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
class Pedido(models.Model):

    estadoChoices = [('Pendiente', 'Pendiente'), ('Completado', 'Completado')]
    
    nombre         = models.CharField(max_length=64)
    cantidad       = models.IntegerField()
    precio_parcial = models.IntegerField()
    estado         = models.CharField(max_length=10, choices = estadoChoices)
    correo         = models.EmailField(max_length=128)    

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades"    