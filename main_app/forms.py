from django.forms import ModelForm
from .models import Feeding
from .models import Pokemon


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ("__all__")


class CapturePokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ('name', 'level', 'img', 'ownedby', 'in_pocket')
# class LevelUpForm(ModelForm):
#     class Meta:
#         model = Pokemon
#         fields = ('level',)
