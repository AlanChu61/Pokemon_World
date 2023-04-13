from django.shortcuts import render
from .models import Pokemon


def home(request):
    return render(request, 'home.html', )


def about(request):
    return render(request, 'about.html', )


def pokemons_view(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/pokemons_view.html', {'pokemons': pokemons, 'title': 'View Your Pokemons'})


def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemons/pokemon_detail.html', {'pokemon': pokemon})
