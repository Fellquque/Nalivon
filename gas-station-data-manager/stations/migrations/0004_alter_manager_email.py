# Generated by Django 4.2.7 on 2023-12-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stations", "0003_alter_discount_options_alter_fuel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manager",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
