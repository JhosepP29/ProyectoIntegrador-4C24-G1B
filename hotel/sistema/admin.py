
from django.contrib import admin
from .models import Administrador
from .models import Cliente
from .models import Habitacion
from .models import Pago
from .models import Reserva

# Register the admin class with the associated model

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    search_fields = ['nombre', 'estado']
    #list_filter = ['nombre']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fec_registro')
    search_fields = ['nombre']

class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'n_habitacion')
    search_fields = ['tipo']

class PagoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'fec_salida')
    search_fields = ['tipo']

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('fec_entrada', 'cant_personas')
    search_fields = ['fec_entrada']

# Register your models here.
admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(Reserva, ReservaAdmin)
