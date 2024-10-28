"""
URL configuration for TiendaVerde project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, formulario, catalogo, sesion, exit, register, carrito, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, envio_pedido

urlpatterns = [
    path('', home, name='home'),
    path('catalogo/', catalogo, name='catalogo'),
    path('formulario', formulario, name='formulario'),
    path('sesion/', sesion, name='sesion'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('carrito/', carrito, name='carrito'),
    path('agregar/<int:Product_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:Product_id>/', eliminar_producto, name="Del"),
    path('restar/<int:Product_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name='CLS'),
    path("pedidos/", envio_pedido, name="pedidos"),
]
