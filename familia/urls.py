from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar_familiar/', views.agregar_familiar, name="agregar_familiar"),
    path('agregar_mascota_perro/', views.agregar_mascota_perro, name="agregar_mascota_perro"),
    path('agregar_mascota_gato/', views.agregar_mascota_gato, name="agregar_mascota_gato"),
    path('borrar_familiar/<identificador>', views.borrar_familiar, name="borrar_familiar"),
    path('borrar_gato/<identificador>', views.borrar_gato, name="borrar_gato"),
    path('borrar_perro/<identificador>', views.borrar_perro, name="borrar_perro"),
    path('buscar/', views.buscar, name="buscar"),
]
