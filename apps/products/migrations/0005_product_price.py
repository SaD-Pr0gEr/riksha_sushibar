# Generated by Django 4.2.10 on 2024-02-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_category_icon_alter_ingredient_icon_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=1000, verbose_name="Price"),
            preserve_default=False,
        ),
    ]
