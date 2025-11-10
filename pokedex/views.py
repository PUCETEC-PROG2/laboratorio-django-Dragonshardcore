from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Pokemon
from .models import Entrenador 
from .forms import PokemonForm
from django.shortcuts import redirect

def index(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons}, request))

def pokemon(request, id:int):
    pokemon=Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def lista_entrenadores(request):
    entrenadores = Entrenador.objects.all()  
    return render(request, 'entrenadores.html', {'entrenadores': entrenadores})

def añadir_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

def editar_pokemon(request, pokemon_id):
    pokemon=Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm( instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})


def eliminar_pokemon(request, pokemon_id):
    pokemon=Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect('index')