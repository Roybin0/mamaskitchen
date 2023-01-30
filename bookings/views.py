from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking


def home(request):
    return render(request, 'index.html')
