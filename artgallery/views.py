from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Producto
from .forms import ProductoForm
from .carrito import Carrito

# Create your views here.
def inicio(request):
    return render(request, 'artgallery/inicio.html')

def obras(request):
    return render(request, 'artgallery/obras.html')

def nosotros(request):
    return render(request, 'artgallery/nosotros.html')

def formulario(request):
    return render(request, 'artgallery/formulario.html')

def api(request):
    return render(request, 'artgallery/api.html')

def politicasdeprivacidad(request):
 return render(request, 'artgallery/politicasdeprivacidad.html')

def politicasdedevolucion(request):
 return render(request, 'artgallery/politicasdedevolucion.html')
def politicasdeenvio(request):
      return render(request, 'artgallery/politicasdeenvio.html')

def terminosyservicios(request):
      return render(request, 'artgallery/terminosyservicios.html')



def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'artgallery/listar_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'artgallery/crear_producto.html', {'form': form})

def actualizar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'artgallery/actualizar_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'artgallery/eliminar_producto.html', {'producto': producto})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_productos')
        else:
            error_message = 'Credenciales inválidas. Por favor, intenta nuevamente.'
            return render(request, 'artgallery/login.html', {'error_message': error_message})
    return render(request, 'artgallery/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def tienda(request):    
    productos = Producto.objects.all()
    return render(request, "artgallery/tienda.html", {'productos': productos,})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")