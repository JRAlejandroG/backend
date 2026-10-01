from django.contrib import admin
from .models import Hotel, Habitacion, Reserva
from .models import Cliente, Empleado, Servicio, Factura, Pago
from .models import TipoHabitacion, TipoServicio, TipoPago
from .models import EstadoReserva, EstadoPago, EstadoFactura
from .models import TipoDocumento, TipoEmpleado, TipoCliente


# Register your models here.x
admin .site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Reserva)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Servicio)
admin.site.register(Factura)
admin.site.register(Pago)
admin.site.register(TipoHabitacion)
admin.site.register(TipoServicio)
admin.site.register(TipoPago)
admin.site.register(EstadoReserva)
admin.site.register(EstadoPago)
admin.site.register(EstadoFactura)
admin.site.register(TipoDocumento)
admin.site.register(TipoEmpleado)
admin.site.register(TipoCliente)
