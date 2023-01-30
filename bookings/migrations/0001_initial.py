# Generated by Django 3.2.16 on 2023-01-30 20:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('party_size', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('date_time', models.DateTimeField()),
                ('special_occasion', models.BooleanField(default=False)),
                ('special_requirements', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
