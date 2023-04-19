# Generated by Django 4.1.7 on 2023-04-18 21:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0011_pokemon_in_pocket"),
    ]

    operations = [
        migrations.RemoveField(model_name="pokemon", name="in_pocket",),
        migrations.AddField(
            model_name="pokemon",
            name="ownedat",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]