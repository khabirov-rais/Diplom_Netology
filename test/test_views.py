
# test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from backend.views import HomeView, CategoryView

class TestHomeView(TestCase):
    def test_home_view_get(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class TestCategoryView(TestCase):
    def test_category_view_get(self):
        client = Client()
        response = client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
