from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from core.models import Product, Pedido
from core.carrito import Carrito
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def formulario(request):
    titulo = "Formulario"
    data = {
        "titulo": titulo
    }
    return render(request,'core/formulario.html', data)

def catalogo(request):
    productos = Product.objects.all()
    return render(request,'core/catalogo.html', {'productos' : productos})

@login_required
def carrito(request):
    productos = Product.objects.all()
    return render(request,'core/carrito.html', {'productos' : productos})

@login_required
def agregar_producto(request, Product_id):
    carrito  = Carrito(request)
    producto = Product.objects.get(id=Product_id)
    carrito.agregar(producto)
    return redirect(request.META.get('HTTP_REFERER', catalogo)) #Se queda en la página actual.

def eliminar_producto(request, Product_id):
    carrito  = Carrito(request)
    producto = Product.objects.get(id=Product_id)
    carrito.eliminar(producto)
    return redirect(catalogo)

def restar_producto(request, Product_id):
    carrito  = Carrito(request)
    producto = Product.objects.get(id=Product_id)
    carrito.restar(producto)
    return redirect(request.META.get('HTTP_REFERER', catalogo)) #Se queda en la página actual.

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(catalogo)




@login_required
def sesion(request):
    titulo = "Sesion"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def exit (request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['email'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('home')

    return render(request, 'registration/register.html', data)

def envio_pedido(request):
    
    if Carrito:
        # Obtener los datos del carrito de la sesión
        carrito = request.session.get('carrito', {})
        correo_usuario = request.user.email # Obtener el usuario logueado
        
        # Recorrer los productos en el carrito y guardar cada uno como un Pedido
        for key, value in carrito.items():
            nameProduct     = value['nombre']
            cantidad        = value['cantidad']
            precio          = value['acumulado']

            # Crear una instancia del modelo Pedido y guardar en la base de datos
            Pedido.objects.all()
            pedido = Pedido(
                nombre         = nameProduct,
                cantidad       = cantidad,
                precio_parcial = precio,
                estado         = "Pendiente",
                correo         = correo_usuario )
            
            pedido.save()
        request.session['carrito'] = {}
        # Redirigir
        return redirect(catalogo)  # Puedes cambiar esta vista según lo que necesites
    else:
        return redirect('carrito')