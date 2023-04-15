from django.urls import path
from . import views
from . models import Pokemon

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('fetch_pokemons/', views.fetch_pokemons, name='fetch_pokemons'),
    path('pokemons/', views.pokemons_view, name='pokemons_view'),
    path('pokemons/<int:pokemon_id>/',
         views.pokemon_detail, name='pokemon_detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
    path('pokemons/<int:pokemon_id>/capture/',
         views.capture_pokemon, name='capture_pokemon'),
    path('pokemon/<int:pokemon_id>/pokemon_level_up/',
         views.level_up, name='pokemon_level_up'),

    path('pokemons/<int:pokemon_id>/add_feeding/',
         views.add_feeding, name='add_feeding'),
]
