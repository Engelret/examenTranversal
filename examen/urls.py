from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('login/', views.login, name="login"),
    path('login/registrar/', views.registrar, name="registrar"),
] 