from django.contrib import admin
from .models import Product, Pedido

# Register your models here.
admin.site.register(Product)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')
    list_filter = ('estado',)  # Filtro por estado

    def get_readonly_fields(self, request, obj=None):
        # Si el usuario no es superusuario, todos los campos excepto 'estado' serán de solo lectura
        if not request.user.is_superuser:
            return ('nombre', 'cantidad', 'precio_parcial', 'correo')
        return ()  # Para superusuarios, permite la edición completa

    def get_fields(self, request, obj=None):
        # Define el orden y selección de campos que se mostrarán
        if not request.user.is_superuser:
            return ('estado',)  # Solo permite 'estado' para usuarios normales
        return ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')
    
admin.site.register(Pedido, PedidoAdmin)    