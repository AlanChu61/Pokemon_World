from django.forms import ModelForm
from .models import Feeding
from .models import Pokemon


class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ('date', 'meal')


# class LevelUpForm(ModelForm):
#     class Meta:
#         model = Pokemon
#         fields = ('level',)
