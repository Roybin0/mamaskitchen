from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'party_size', 'date_time',
                    'special_occasion', 'special_requirements', 'confirmed')
    search_fields = ('name', 'confirm', 'email')
    list_filter = ('name', 'party_size')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(confirmed=True)
