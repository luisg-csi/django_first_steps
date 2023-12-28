# myapp/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
import pytest_django
"""
@pytest.mark.django_db
class TestMyViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_home_view_authenticated(self):
        # Prueba para verificar que la vista home se carga correctamente para usuarios autenticados
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the home page!')
        self.client.logout()

    def test_home_view_unauthenticated(self):
        # Prueba para verificar que la vista home se redirige a la página de inicio de sesión para usuarios no autenticados
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('home'))

    def test_another_view(self):
        # Agrega más pruebas según tus necesidades
        pass"""
