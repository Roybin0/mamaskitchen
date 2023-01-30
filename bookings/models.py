from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    date_time = models.DateTimeField()
    special_occasion = models.BooleanField(default=False)
    special_requirements = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking request from {self.name} for {self.party_size} people"
