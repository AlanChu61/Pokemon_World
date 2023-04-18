import requests
from .models import Pokemon
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm, CapturePokemonForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html', {'title': 'HomePage'})


def about(request):
    return render(request, 'about.html', {'title': 'AboutPage'})


@login_required
def pokemons_view(request):
    pokemons = Pokemon.objects.filter(ownedby=request.user)
    return render(request, 'pokemons/pokemons_view.html', {'pokemons': pokemons, 'title': 'View Your Pokemons'})


def pokemon_detail(request, pokemon_id):
    feeding_form = FeedingForm()
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemons/pokemon_detail.html', {'pokemon': pokemon, 'title': 'Pokemon Detail', 'user': request.user, 'feeding_form': feeding_form})


def level_up(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        pokemon.level_up()
        return redirect('pokemon_detail', pokemon_id=pokemon.id)


def pokemon_pocket_box(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    print(pokemon.name)
    print(pokemon.in_pocket)
    if request.method == 'POST':
        if pokemon.in_pocket:
            pokemon.in_pocket = False
        else:
            pokemon.in_pocket = True
        pokemon.save()
        return redirect('pokemons_view')


def check_evolve(pokemon_id):
    url = f'https://pokeapi.co/api/v2/evolution-chain/{id}'
    response = requests.get(url)
    data = response.json()
    evole_trigger = data['chain']['evolves_to'][0]['evolution_details'][0]['trigger']['name']
    min_level = data['chain']['evolves_to'][0]['evolution_details'][0]['min_level']
    print(evole_trigger, min_level)


def capture_pokemon(request, pokemon_id):
    capture_pokemon_id = request.POST.get('pokemon_id')
    captured_pokemon = fetch_pokemon(capture_pokemon_id)
    name = captured_pokemon['name']
    id = captured_pokemon['id']
    level = 5
    img = captured_pokemon['img']
    ownedby = request.user
    in_pocket = True if len(
        Pokemon.objects.filter(in_pocket=True)) < 6 else False
    new_pokemon = CapturePokemonForm(
        {'name': name, 'level': level, 'img': img, 'ownedby': ownedby, 'ownedat': ownedat, 'in_pocket': in_pocket})
    new_pokemon.save()
    return redirect('fetch_pokemons')


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/pokemons/'
    template_name = 'pokemons/pokemon_form.html'


class PokemonRelease(DeleteView):
    model = Pokemon
    success_url = '/pokemons/'
    template_name = 'pokemons/pokemon_confirm_delete.html'


def fetch_pokemon(id):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    response = requests.get(url)
    data = response.json()
    pokemon = {
        'name': data['forms'][0]['name'].capitalize(),
        'id': data['id'],
        'img': data['sprites']['other']['official-artwork']['front_default'],
    }
    return pokemon


def fetch_pokemons(request):
    pokemons = []
    for i in range(1, 30):
        pokemon = fetch_pokemon(i)
        pokemons.append(pokemon)
    return render(request, 'pokemons/fetch_pokemons.html', {'pokemons': pokemons, 'title': 'Fetch Pokemons'})


def add_feeding(request, pokemon_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pokemon_id = pokemon_id
        new_feeding.save()
        pokemon = Pokemon.objects.get(id=pokemon_id)
        pokemon.is_level_up()
    return redirect('pokemon_detail', pokemon_id=pokemon_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
