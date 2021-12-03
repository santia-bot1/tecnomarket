from django.shortcuts import render, get_object_or_404, redirect
from .models import Productos
from .forms import ContactoForm, ProductoForm
from django.contrib import messages


# Create your views here.
def home(request):
    productos = Productos.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)


def contacto(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Contacto guardado.'
        else:
            data['form'] = formulario
    return render(request, 'app/contacto.html', data)


def galeria(request):
    return render(request, "app/galeria.html")


def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Guardado Exitosamente!')

        else:
            data["form"] = formulario
    return render(request, 'productos/agregar.html', data)


def listar_productos(request):
    productos = Productos.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'productos/listar.html', data)


def modificar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, ' Modificado correctamente!')
            return redirect(to='listar_productos')
        else:
            data['form'] = formulario
    return render(request,'productos/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Productos, id=id)
    producto.delete()
    messages.success(request, 'Eliminado Satisfactoriamente!')
    return redirect(to='listar_productos')