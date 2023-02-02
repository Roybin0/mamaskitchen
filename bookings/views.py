from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Booking, Customer
from .forms import BookingForm
from datetime import datetime, timedelta


def home(request):
    return render(request, 'index.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def booking(request):
    if request.method == 'GET':
        return render(request, 'booking.html')

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email'):
            booking_form = Booking()
            booking_form.name = request.POST.get('name')
            booking_form.email = request.POST.get('email')
            booking_form.phone = request.POST.get('phone')
            booking_form.party_size = request.POST.get('party_size')
            booking_form.date = request.POST.get('date')
            booking_form.time = request.POST.get('time')
            if request.POST.get('special_occasion') == 'on':
                booking_form.special_occasion == 'True'
            else:
                booking_form.special_occasion == 'False'
            if request.POST.get('special_occasion') == 'on':
                booking_form.special_requirements == 'True'
            else:
                booking_form.special_requirements == 'False'
            booking_form.confirmed = False
            booking_form.save()
            return render(request, 'thankyou.html')
        else:
            return render(request, 'booking.html')


# Check for available seats - 40 seats available per hour
def isSpaceAvailable(time):
    maxSeats = 40
    seatsTaken = ()
    for hour in time:
        if Booking.objects.filter(confirmed=True):
            if hour == Booking.objects.time:
                seatsTaken.append(Booking.objects.party_size)
    availableSeats = maxSeats - sum(seatsTaken)
    return availableSeats
