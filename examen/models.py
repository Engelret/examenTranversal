from django.db import models

# Create your models here.
class Producto(models.Model):
    nombreProducto = models.CharField(max_length = 60)
    presupuesto = models.CharField(max_length = 40)
    costoReal = models.ImageField(upload_to = 'fotos/')
    tienda = models.TextField(max_length = 200)
    notaAdicional = models.CharField(max_length = 50)

    def __str__(self):
        return "producto"

class Persona(models.Model):
    run = models.CharField(max_length = 10)
    correo = models.CharField(max_length = 60)
    nombre = models.CharField(max_length = 100)
    fechaNac = models.CharField(max_length = 10)
    telefono = models.BigIntegerField()
    nombreUsuario = models.CharField(max_length = 40)
    contraseñaUsuario = models.CharField(max_length = 50)
    region = models.CharField(max_length = 60)
    comuna = models.CharField(max_length = 60)

    def __str__(self):
        return "persona"