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
    path('lista/', views.HotellistView.as_view(), name='lista_hoteles'),
    path('crear/', views.HotelCreateView.as_view(), name='crear_hotel'),
    path('editar/<int:pk>/', views.HotelUpdateView.as_view(), name='editar_hotel'),
    path('cambiar-estado/<int:pk>/', views.cambiar_estado_hotel, name='cambiar_estado_hotel'),
]