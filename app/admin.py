from django.contrib import admin
from.models import *


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock', 'tipo']
    search_fields = ['codigo']
    list_per_page = 3



class MascotaAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','raza','años','tipo']
    search_fields = ['codigo']
    list_per_page = 3


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['rut','nombre','contraseña','mail','tipo']
    search_fields = ['rut']
    list_per_page = 3
    




admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)

admin.site.register(Mascota,MascotaAdmin)
admin.site.register(TipoMascota)

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(TipoCliente)