# Generated by Django 4.2.7 on 2023-11-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='is_active',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=50, null=True),
        ),
    ]
