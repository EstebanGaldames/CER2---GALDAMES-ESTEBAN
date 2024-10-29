from django.contrib import admin
from .models import Product, Pedido

# Register your models here.
admin.site.register(Product)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')
    list_filter  = ('estado',)  # Filtro por estado

    def get_readonly_fields(self, request, obj=None):
        # Si el usuario no es superusuario, solo estado se podrá modificar.
        if not request.user.is_superuser:
            return ('nombre', 'cantidad', 'precio_parcial')
        return ('correo',)  # Para superusuarios puede modificar todo excepto el correo.

    def get_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('estado',)  # Solo permite estado para usuarios vendedores.
        return ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')
    
admin.site.register(Pedido, PedidoAdmin)    