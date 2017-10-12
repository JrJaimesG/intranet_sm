from django.contrib import admin
from .models import Solicitud, Vehiculo, Chofer, Asignacion, Bitacora

admin.site.register(Solicitud)
admin.site.register(Vehiculo)
admin.site.register(Chofer)
admin.site.register(Asignacion)
admin.site.register(Bitacora)
# Register your models here.
