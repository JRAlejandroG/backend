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

    # Hoteles
    path('lista/', views.HotellistView.as_view(), name='lista_hoteles'),
    path('crear/', views.HotelCreateView.as_view(), name='crear_hotel'),
    path('editar/<int:pk>/', views.HotelUpdateView.as_view(), name='editar_hotel'),
    path('cambiar-estado/<int:pk>/', views.cambiar_estado_hotel, name='cambiar_estado_hotel'),

    # Gestion del hotel
    path('gestion/<int:pk>/', views.gestion_hotel, name='gestion_hotel'),

    # Habitaciones
    path('gestion/<int:pk>/habitacion/crear/', views.HabitacionCreateView.as_view(), name='crear_habitacion'),
    path('habitacion/<int:pk>/editar/', views.HabitacionUpdateView.as_view(), name='editar_habitacion'),
    path('habitacion/<int:pk>/eliminar/', views.HabitacionDeleteView.as_view(), name='eliminar_habitacion'),
]