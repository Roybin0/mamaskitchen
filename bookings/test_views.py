from django.test import TestCase
from .models import Booking


class TestViews(TestCase):

    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_menu_page_loads(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
