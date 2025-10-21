from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Pokemon
from .models import Entrenador 
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
