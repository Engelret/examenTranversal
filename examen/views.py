from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Producto, Persona


# Create your views here.
def index(request):
    return render(request,'index.html',{})

# Registro producto
def registroProducto(request):
    return render(request,'index.html',{'producto': Producto.objects.all()})

def agregarProducto(request):
    nombreProducto = request.POST.get('nombre','')
    presupuesto = request.POST.get('presupuesto','')
    costoReal = request.FILES.get('costo','')
    tienda = request.POST.get('tienda','')
    notaAdicional = request.POST.get('nota','')

    producto = Producto(nombreProducto = nombre, presupuesto = presupuesto, costoReal = costo, tienda = tienda, notaAdicional = nota )
    producto.save()
    
    return redirect('index')

# Registro persona
def registroPersona(request):
    return render(request, 'index.html',{'persona': Persona.objects.all()})

def crearPersona(request):
    run = request.POST.get('run','')
    correo = request.POST.get('correo','')
    nombre = request.POST.get('nombre','')
    fechaNac = request.POST.get('fechaNac','')
    telefono = request.POST.get('telefono','')
    nombreUsuario = request.POST.get('nombreUsuario','')
    contraseñaUsuario = request.POST.get('contraseñaUsuario','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')

    persona = Persona(run=run ,correo=correo ,nombre=nombre ,fechaNac=fechaNac ,telefono=telefono ,nombreUsuario=nombreUsuario ,contraseñaUsuario=contraseñaUsuario ,region=region ,comuna=comuna )
    persona.save()

    user = User.objects.create_user(nombreUsuario, correo, contraseñaUsuario)
    user.save()
    
    return redirect('index')
