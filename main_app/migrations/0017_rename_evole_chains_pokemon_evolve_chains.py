# Generated by Django 4.1.7 on 2023-04-19 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0016_pokemon_evole_chains"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pokemon", old_name="evole_chains", new_name="evolve_chains",
        ),
    ]