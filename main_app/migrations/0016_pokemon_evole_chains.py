# Generated by Django 4.1.7 on 2023-04-19 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0015_pokemon_pokemon_id_alter_pokemon_ready_to_level_up"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="evole_chains",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]