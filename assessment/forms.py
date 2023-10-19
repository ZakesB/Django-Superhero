from django import forms
from .models import SuperHero


class SuperHeroForm(forms.ModelForm):
    class Meta:
        model = SuperHero
        fields = ['name', 'alignment', 'height', 'weight']
