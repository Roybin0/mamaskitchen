from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Booking


def home(request):
    return render(request, 'index.html')


def booking(View):
    return render(request, 'booking.html')
