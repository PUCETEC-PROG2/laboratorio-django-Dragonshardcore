from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Pokemon , Entrenador 
from .forms import PokemonForm


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
@login_required
def añadir_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
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

@login_required
def eliminar_pokemon(request, pokemon_id):
    pokemon=Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect('index')

class CustomerLoginView(LoginView):
    template_name= 'login_form.html'
    

   