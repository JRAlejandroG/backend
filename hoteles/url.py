from django.urls import path, include
from rest_framework import routers
from hoteles import views

enrutador = routers.DefaultRouter()
enrutador.register(r'hoteles', views.HotelViewSet)
enrutador.register(r'habitaciones', views.HabitacionViewSet)
enrutador.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', include(enrutador.urls)),
]