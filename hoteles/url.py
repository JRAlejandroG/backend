from django.urls import path, include
from rest_framework import routers
from hoteles import views

enrutador = routers.DefaultRouter()

enrutador.register(r'hotel', views.HotelViewSet)
enrutador.register(r'habitaciones', views.HabitacionViewSet)
enrutador.register(r'reservas', views.ReservaViewSet)
enrutador.register(r'huespedes', views.HuespedViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]