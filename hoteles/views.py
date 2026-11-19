from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.views.decorators.http import require_POST
from rest_framework import viewsets

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


@require_POST
def cambiar_estado_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    hotel.activo = not hotel.activo
    hotel.save()

    return redirect('lista_hoteles')


def gestion_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)

    habitaciones = hotel.habitaciones.all().order_by('piso', 'numero')

    pisos = {}
    for habitacion in habitaciones:
        pisos.setdefault(habitacion.piso, []).append(habitacion)

    return render(request, 'hoteles/gestion_hotel.html', {
        'hotel': hotel,
        'pisos': pisos,
    })


class HabitacionCreateView(CreateView):
    model = Habitacion
    template_name = 'hoteles/crear_habitacion.html'
    fields = [
        'numero',
        'piso',
        'tipo',
        'estado',
        'capacidad_personas',
        'precio_por_noche',
        'detalles',
    ]

    def form_valid(self, form):
        hotel = get_object_or_404(Hotel, pk=self.kwargs['pk'])
        form.instance.hotel = hotel
        form.instance.disponible = form.instance.estado == 'DIS'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gestion_hotel', kwargs={'pk': self.kwargs['pk']})


class HabitacionUpdateView(UpdateView):
    model = Habitacion
    template_name = 'hoteles/editar_habitacion.html'
    fields = [
        'numero',
        'piso',
        'tipo',
        'estado',
        'capacidad_personas',
        'precio_por_noche',
        'detalles',
    ]

    def form_valid(self, form):
        form.instance.disponible = form.instance.estado == 'DIS'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('gestion_hotel', kwargs={
            'pk': self.object.hotel.pk
        })


class HabitacionDeleteView(DeleteView):
    model = Habitacion
    template_name = 'hoteles/eliminar_habitacion.html'

    def get_success_url(self):
        return reverse('gestion_hotel', kwargs={
            'pk': self.object.hotel.pk
        })