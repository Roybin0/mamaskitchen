from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'party_size', 'date', 'time',
                    'booking_ref', 'special_occasion', 'special_requirements',
                    'confirmed')
    search_fields = ('name', 'confirm', 'email', 'date')
    list_filter = ('name', 'party_size', 'date')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(confirmed=True)


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):

#     list_display = ('name', 'email', 'phone')
#     search_fields = ('name', 'email')
