from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path('añadir_pokemon/', views.añadir_pokemon, name='añadir_pokemon'),
    path('entrenadores/', views.lista_entrenadores, name='lista_entrenadores'),
    path('editar_pokemon/<int:pokemon_id>/', views.editar_pokemon, name='editar_pokemon'),
    path('eliminar_pokemon/<int:pokemon_id>/', views.eliminar_pokemon, name='eliminar_pokemon'),
    
]

