from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


TIME_CHOICES = (
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
)


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    party_size = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    special_occasion = models.BooleanField(default=False)
    special_requirements = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking request from {self.name} for {self.party_size} people"


class Customer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.customer.name