# Generated by Django 4.1.7 on 2023-04-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0002_remove_pokemon_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon", name="img", field=models.CharField(max_length=200),
        ),
    ]