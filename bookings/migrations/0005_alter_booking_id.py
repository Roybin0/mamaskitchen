# Generated by Django 3.2.16 on 2023-02-03 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
