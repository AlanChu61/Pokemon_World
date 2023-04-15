from django.contrib import admin
from .models import Pokemon
from .models import Feeding, Player
admin.site.register(Pokemon)
admin.site.register(Feeding)
admin.site.register(Player)
