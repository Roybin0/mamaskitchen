from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Booking, Customer
from .forms import BookingForm


def home(request):
    return render(request, 'index.html')


def thankyou(request):
    return render(request, 'thankyou.html')


# def booking(request):
#     if request.method == 'GET':
#         return render(request, 'booking.html')

#     if request.method == 'POST':
#         if isSpaceAvailable(request.POST.get('time')) < 40:
#             booking_form = Booking()
#             booking_form.name = request.POST.get('name')
#             booking_form.email = request.POST.get('email')
#             booking_form.phone = request.POST.get('phone')
#             booking_form.party_size = request.POST.get('party_size')
#             booking_form.date = request.POST.get('date')
#             booking_form.time = request.POST.get('time')
#             if request.POST.get('special_occasion') == 'on':
#                 booking_form.special_occasion == 'True'
#             else:
#                 booking_form.special_occasion == 'False'
#             if request.POST.get('special_occasion') == 'on':
#                 booking_form.special_requirements == 'True'
#             else:
#                 booking_form.special_requirements == 'False'
#             booking_form.confirmed = False
#             booking_form.save()

#             customer = Customer()
#             customer.name = request.POST.get('name')
#             customer.email = request.POST.get('email')
#             customer.phone = request.POST.get('phone')
#             customer.save()

#             return render(request, 'thankyou.html')
#         else:
#             return render(request, 'booking.html')


def booking(request):

    if request.method == 'POST':
        booking = BookingForm(request.POST)
        if booking.is_valid():
            if int(request.POST.get('party_size')) > isSpaceAvailable(
                    request.POST.get('date'), request.POST.get('time')):
                messages.add_message(
                    request, messages.ERROR, 'There are no tables available at\
                        this time. Choose another time or date.')
            else:
                booking.save()
                return HttpResponseRedirect('/thanks/')
    else:
        booking = BookingForm()

    return render(request, 'booking.html', {'booking_form': booking})


# Check for available seats - 40 seats available per hour
def isSpaceAvailable(date, time):

    maxSeats = 40
    seatsTaken = 0
    bookings_by_date = Booking.objects.filter(date=date)
    bookings_by_time = bookings_by_date.filter(time=time)
    for booking in bookings_by_time:
        seatsTaken = seatsTaken + booking.party_size
    availableSeats = maxSeats - seatsTaken
    return availableSeats


# def edit_booking(request, email):
#     booking = get_object_or_404(Booking, email=email)
#     if request.method == 'POST':
#         form = BookingForm()
