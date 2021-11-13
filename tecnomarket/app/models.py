from django.db import models


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripciones = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to='productos', null=True)

    def __str__(self):
        return self.nombre


opciones_consultas = [
    [0, 'Consultas'],
    [1, 'Reclamo'],
    [2, 'Sugerencia'],
    [3, 'Felicitaciones']
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
