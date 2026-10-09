from rest_framework import serializers
from .models import Hotel, Habitacion, Huesped, Reserva

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        #fields = '__all__' esto es para que muestre todos los campos de la tabla
        fields = ['nombre', 'direccion', 'telefono', 'email', 'descripcion', 'created_at', 'updated_at']

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['hotel', 'numero', 'tipo', 'capacidad_personas', 'precio_por_noche', 'disponible', 'detalles', 'created_at', 'updated_at']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['huesped', 'habitacion', 'fecha_inicio', 'fecha_fin', 'estado', 'created_at', 'updated_at']

class HuespedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huesped
        fields = ['nombre', 'apellido', 'documento_identidad', 'email', 'telefono', 'created_at', 'updated_at']
