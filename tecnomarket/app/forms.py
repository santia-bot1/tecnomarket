from django import forms
from django.forms import DateInput

from .models import Contacto, Productos


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class DatInput(forms.DateInput):
    input_type = 'date'


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'fecha_fabricacion': DateInput(),
        }


