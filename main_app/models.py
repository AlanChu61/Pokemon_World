from django.db import models
from datetime import date
from django.contrib.auth.models import User
import requests

default_items = {'thunder-stone': 1}


class Player(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(
        max_length=250, default="https://www.kocpc.com.tw/wp-content/uploads/2016/09/1473059862-1058abae0dc372f4432cbea7fa123512.jpg")
    money = models.IntegerField(default=5000)
    items = models.JSONField(default=default_items)
    ownedby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    pokemon_id = models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    level = models.IntegerField(default=5)
    evolve_chains = models.JSONField()
    ownedby = models.ForeignKey(User, on_delete=models.CASCADE)
    ownedat = models.DateField(auto_now_add=True)
    in_pocket = models.BooleanField(default=True)
    # level up
    is_leveled = models.BooleanField(default=False)
    ready_to_level_up = models.BooleanField(default=False)
    # evolve
    ready_to_evolve = models.BooleanField(default=False)
    # skills = models.charField(Skill)

    def __str__(self):
        return self.name

    def is_level_up(self):
        meals = self.feeding_set.filter(date=date.today())
        good_eat = 0
        for item in meals:
            if item.meal == "B" or item.meal == "L" or item.meal == "D":
                good_eat += 1
            if item.meal == "S" or item.meal == "T":
                good_eat += 0.5
        if good_eat >= 3:
            self.ready_to_level_up = True
            good_eat = 0
            self.save()

    def level_up(self):
        self.level += 1
        self.ready_to_level_up = False
        self.is_leveled = True
        self.save()

    def evolve(self, evolve_to):
        self.name = evolve_to
        url = f'https://pokeapi.co/api/v2/pokemon/{evolve_to}'
        response = requests.get(url)
        data = response.json()
        self.img = data['sprites']['other']['official-artwork']['front_default']
        self.save()


class Feeding(models.Model):
    MEALS = (
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("S", "Snack"),
        ("D", "Dinner"),
        ("T", "Treat"),
    )
    date = models.DateField("Feeding Date")
    meal = models.CharField(
        max_length=1, choices=MEALS, default=MEALS[-1][0], verbose_name="Meal Type")
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
