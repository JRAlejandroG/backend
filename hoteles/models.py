from django.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    categoria_estrellas = models.IntegerField(default=5)
    telefono = models.CharField(max_length=20)
    email_contacto = models.EmailField()
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Habitacion(models.Model):
    TIPOS_HABITACION = [
        ('IND', 'Individual'),
        ('DOB', 'Doble'),
        ('SUI', 'Suite Temática LaManchaland'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='habitaciones')
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=3, choices=TIPOS_HABITACION, default='IND')
    capacidad_personas = models.IntegerField(default=2)
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    detalles = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Habitación {self.numero} - {self.hotel.nombre}"


class Huesped(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento_identidad = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Reserva(models.Model):
    ESTADOS_RESERVA = [
        ('PEN', 'Pendiente'),
        ('CON', 'Confirmada'),
        ('CAN', 'Cancelada'),
        ('FIN', 'Finalizada'),
    ]

    huesped = models.ForeignKey(Huesped, on_delete=models.CASCADE, related_name='reservas')
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='reservas')
    fecha_check_in = models.DateField()
    fecha_check_out = models.DateField()
    estado = models.CharField(max_length=3, choices=ESTADOS_RESERVA, default='PEN')
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reserva #{self.id} - {self.huesped}"