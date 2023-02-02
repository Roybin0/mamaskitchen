from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'party_size', 'date', 'time',
                  'special_occasion', 'special_requirements',)
