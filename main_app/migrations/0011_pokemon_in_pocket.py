# Generated by Django 4.1.7 on 2023-04-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0010_pokemon_ownedby"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="in_pocket",
            field=models.BooleanField(default=True),
        ),
    ]
