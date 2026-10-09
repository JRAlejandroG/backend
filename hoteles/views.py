from django.shortcuts import render
from rest_framework import viewsets

from .models import Hotel, Habitacion, Huesped, Reserva

from .serializer import HotelSerializer, HabitacionSerializer, HuespedSerializer, ReservaSerializer

def home(request):
    return render(request, 'hoteles/index.html')

def pagina_no_encontrada(request, exception):
    return render(request, 'hoteles/404.html', status=404)

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer
