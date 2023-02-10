from django.test import TestCase
from .models import Booking


class TestViews(TestCase):

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_privacy_page_loads(self):
        response = self.client.get('/privacy-policy')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy.html')

    def test_menu_page_loads(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_contact_page_loads(self):
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_booking_page_loads(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_booking_ref_page_loads_edit(self):
        response = self.client.get('/edit-booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-booking-reference.html')

    def test_booking_ref_page_loads_delete(self):
        response = self.client.get('/cancel-booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete-booking-reference.html')

    def test_edit_booking_page_loads(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        response = self.client.get(f'/edit-booking/{booking.booking_ref}', {'name': 'Updated Name'})
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-booking.html')

    def test_can_edit_booking(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        response = self.client.post(f'/edit-booking/{booking.booking_ref}', {'phone': 54321})
        self.assertRedirects(response, '/')
        updated_booking = Booking.objects.get(booking_ref=booking.booking_ref)
        self.assertEqual(updated_booking.phone, 54321)

    def test_user_confirmation_before_delete(self):
        booking = Booking.objects.create(name='Test', phone=12345)
        response = self.client.get(f'/cancel-booking/{booking.booking_ref}')
        self.assertTemplateUsed(response, 'cancel-confirmation.html')
        existing_bookings = Booking.objects.filter(booking_ref=booking.booking_ref)
        self.assertEqual(len(existing_bookings), 0)
    
    
