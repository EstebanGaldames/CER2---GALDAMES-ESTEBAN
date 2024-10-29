from django.contrib import admin
from .models import Product, Pedido

# Register your models here.
admin.site.register(Product)

class PedidoAdmin(admin.ModelAdmin):
    lista = ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')
    filtroLista = ('estado')  # Filtro por estado

    def getCamposVendedor(self, request, obj=None):
        # Si el usuario no es superusuario, solo es estado se podrá modificar.
        if not request.user.is_superuser:
            return ('nombre', 'cantidad', 'precio_parcial', 'correo')
        return ()  # Para superusuarios puede modificar todo.

    def getCampos(self, request, obj=None):
        if not request.user.is_superuser:
            return ('estado',)  # Solo permite estado para usuarios vendedores.
        return ('nombre', 'cantidad', 'precio_parcial', 'estado', 'correo')
    
admin.site.register(Pedido, PedidoAdmin)    