from rest_framework import serializers
from .models import Hotel, Habitacion, Reserva
from .models import Cliente, Empleado, Servicio, Factura, Pago
from .models import TipoHabitacion, TipoServicio, TipoPago
from .models import EstadoReserva, EstadoPago, EstadoFactura
from .models import TipoDocumento, TipoEmpleado, TipoCliente

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        #fields = '__all__' esto es para que muestre todos los campos de la tabla
        fields = ['nombre', 'direccion', 'telefono', 'email', 'descripcion', 'created_at', 'updated_at']
        