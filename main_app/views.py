import requests
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
    return render(request, 'pokemons/pokemon_detail.html', {'pokemon': pokemon, 'title': 'Pokemon Detail'})


def fetch_pokemons(request):
    pokemons = []
    for i in range(1, 10):
        url = f'https://pokeapi.co/api/v2/pokemon/{i}'
        response = requests.get(url)
        data = response.json()
        pokemon = {
            'name': data['forms'][0]['name'].capitalize(),
            'id': data['id'],
            'img': data['sprites']['other']['official-artwork']['front_default'],
        }
        pokemons.append(pokemon)
    return render(request, 'pokemons/fetch_pokemons.html', {'pokemons': pokemons, 'title': 'Fetch Pokemons'})
