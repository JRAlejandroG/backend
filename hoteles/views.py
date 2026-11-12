from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets
from django.views.generic import ListView, CreateView
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST


from .models import Hotel, Habitacion, Huesped, Reserva

from .serializer import (
    HotelSerializer,
    HabitacionSerializer,
    HuespedSerializer,
    ReservaSerializer
)


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


class HotellistView(ListView):
    model = Hotel
    template_name = 'hoteles/lista_hoteles.html'
    context_object_name = 'hoteles'
    queryset = Hotel.objects.all()


class HotelCreateView(CreateView):
    model = Hotel
    template_name = 'hoteles/crear_hotel.html'
    fields = [
        'nombre',
        'direccion',
        'categoria_estrellas',
        'telefono',
        'email_contacto',
        'descripcion',
    ]
    success_url = '/hoteles/lista/'

class HotelUpdateView(UpdateView):
    model = Hotel
    template_name = 'hoteles/editar_hotel.html'
    fields = [
        'nombre',
        'direccion',
        'categoria_estrellas',
        'telefono',
        'email_contacto',
        'descripcion',
    ]
    success_url = '/hoteles/lista/'

    # Activar o desactivar hotel
@require_POST
def cambiar_estado_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    hotel.activo = not hotel.activo
    hotel.save()

    return redirect('lista_hoteles')
