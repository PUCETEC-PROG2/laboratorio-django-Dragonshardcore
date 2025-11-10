from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre del Pokémon',
            'type': 'Tipo',
            'level': 'Nivel',
            'image': 'Imagen',
            'height': 'Altura',
            'weight': 'Peso',
            'trainer': 'Entrenador',
            }

widget = {
    'name': forms.TextInput(attrs={'class': 'form-control'}),
    'type': forms.TextInput(attrs={'class': 'form-control'}),
    'level': forms.NumberInput(attrs={'class': 'form-control'}),
    'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    'height': forms.NumberInput(attrs={'class': 'form-control'}),
    'weight': forms.NumberInput(attrs={'class': 'form-control'}),
    'trainer': forms.Select(attrs={'class': 'form-control'}),
}