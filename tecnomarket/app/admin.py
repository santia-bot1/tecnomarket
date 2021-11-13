from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Marca, Productos, Contacto


# Register your models here.


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '80'})}
    }


@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'nuevo', 'marca']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_filter = ['marca', 'nuevo']
    list_per_page = 5


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'tipo_consulta', 'avisos']
    list_editable = ['correo']
    search_fields = ['nombre', 'correo']
    list_filter = ['tipo_consulta', 'avisos']
    list_per_page = 3
