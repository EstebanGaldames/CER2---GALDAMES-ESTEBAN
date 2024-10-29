from django.shortcuts import render, redirect
#Login y Logout.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
#Modelos y carrito.
from core.models import Product, Pedido
from core.carrito import Carrito
#Form del usuario.
from .forms import CustomUserCreationForm


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
def logine(request):
    titulo = "Login"
    data = {
        "titulo": titulo
    }
    return render(request,'core/login.html', data)

def exit (request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form' : CustomUserCreationForm() #Formulario de registro.
    }

    if request.method == 'POST': #Verifico que sea post.
        user_creation_form = CustomUserCreationForm(data=request.POST)  #Creo una instancia con los datos de post

        if user_creation_form.is_valid(): #Verifico que todos los datos entregados sean válidos.
            user_creation_form.save() #Lo guardo

            user = authenticate(username=user_creation_form.cleaned_data['email'], password=user_creation_form.cleaned_data['password1']) #Logeo al usuario con el email y contraseña.
            login(request, user) #Inicio sesión.

            return redirect('home') #Lo redirecciono al home.

    return render(request, 'registration/register.html', data)

def envio_pedido(request):

    carro = request.session.get('carrito', {})

    #Si el carrito no está vacío.
    if carro:
        #Obtengo los datos del carrito.
        carrito = request.session.get('carrito', {})
        correo_usuario = request.user.email # Obtengo el usuario logeado.
        
        #For que recorre los productos en el carrito y los guarda en pedidos
        for key, value in carrito.items():
            nameProduct     = value['nombre']
            cantidad        = value['cantidad']
            precio          = value['acumulado']

            #Crear una instancia del modelo Pedido y guardar en la base de datos
            Pedido.objects.all()
            pedido = Pedido(
                nombre         = nameProduct,
                cantidad       = cantidad,
                precio_parcial = precio,
                estado         = "Pendiente",
                correo         = correo_usuario )
            
            #Guardo el pedido
            pedido.save()

        #Limpio el carrito.    
        request.session['carrito'] = {}

        #Redirigo al catalogo.
        return redirect(catalogo) 
    else:
        return redirect('carrito')