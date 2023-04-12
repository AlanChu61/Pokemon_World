from django.shortcuts import render


def home(request):
    return render(request, 'home.html', )


def about(request):
    return render(request, 'about.html', )


def pokemons_view(request):
    return render(request, 'pokemons/pokemons_view.html', )
