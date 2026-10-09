from django.contrib import admin
from .models import Hotel, Habitacion, Reserva, Huesped


# Register your models here.x
admin .site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Huesped)