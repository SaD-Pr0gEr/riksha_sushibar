# Generated by Django 4.2.10 on 2024-02-13 12:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ingredient",
            options={
                "verbose_name": "Ingredient",
                "verbose_name_plural": "Ingredients",
            },
        ),
    ]
