from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('pokemons/', views.pokemons_view, name='pokemons_view'),
    path('pokemons/<int:pokemon_id>/',
         views.pokemon_detail, name='pokemon_detail'),
]
