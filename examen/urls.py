from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    # urls agregar producto
    path('registroProducto/',views.registroProducto, name="registroProducto"),
    path('registroProducto/agregarProducto/',views.agregarProducto, name="agregarProducto"),
     # urls agregar persona
    path('registroPersona/',views.registroPersona, name="registroPersona"),
    path('registroPersona/crearPersona/',views.crearPersona, name="crearPersona"),
]