# Generated by Django 4.2.7 on 2024-02-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_groups_user_user_permissions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=150, verbose_name="first name"),
        ),
    ]
