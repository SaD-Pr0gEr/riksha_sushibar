# Generated by Django 4.2.10 on 2024-02-13 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_alter_ingredient_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productattribute",
            name="attribute",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attribute_products",
                to="products.attribute",
                verbose_name="Attribute",
            ),
        ),
    ]
