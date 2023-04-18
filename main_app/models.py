from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=100)
    ownedby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    level = models.IntegerField(default=5)
    ownedby = models.ForeignKey(User, on_delete=models.CASCADE)
    ownedat = models.DateField(auto_now_add=True)
    in_pocket = models.BooleanField(default=True)
    # skills = models.charField(Skill)

    ready_to_level_up = models.BooleanField(default=True)

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

    def level_up(self):
        self.level += 1
        self.ready_to_level_up = False
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
