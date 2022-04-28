from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name="index"),
    path('gatos1/', gatos1 ,name="gato"),
    path('perro1/', perro1 ,name="perro"),
    path('exotico1/', exotico1 ,name="exotico"),
    path('sinregistro/', sinregistro ,name="sinregistro"),




    path('perro1con/', perro1con ,name="perro1con"),
    path('gatos1con/', gatos1con ,name="gatos1con"),
    path('exotico1con/', exotico1con ,name="exotico1con"),
    path('fundacion/', fundacion ,name="fundacion"),
    path('historial/', historial ,name="historial"),
    path('segui/', segui ,name="segui"),
    path('vercarro/', vercarro ,name="vercarro"),


]
