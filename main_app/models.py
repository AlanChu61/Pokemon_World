from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Player(models.Model):
    name = models.CharField(max_length=100)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    level = models.IntegerField()
    # skills = models.charField(Skill)
    # owner = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def fed_for_today(self):
    #     return self.feeding_set.filter(date=date.today()).count() >= 3


# class Feeding(models.Model):
#     MEALS = (
#         ("B", "Breakfast"),
#         ("L", "Lunch"),
#         ("S", "Snack"),
#         ("D", "Dinner"),
#         ("T", "Treat"),
#     )
#     date = models.DateField("Feeding Date")
#     meal = models.CharField(
#         max_length=1, choice=MEALS, default=MEALS[0][0], verbose_name="Meal Type")
#     pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.get_meal_display()} on {self.date}"

#     class Meta:
#         ordering = ["-date"]
