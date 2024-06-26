# Generated by Django 4.2.7 on 2023-11-23 12:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_alter_discount_is_active_alter_transaction_total'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ['discount']},
        ),
        migrations.AlterModelOptions(
            name='fuel',
            options={'ordering': ['price'], 'verbose_name': 'fuel', 'verbose_name_plural': 'fuel'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'manager', 'verbose_name_plural': 'managers'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(99.99)]),
        ),
    ]
