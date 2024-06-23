from django.test import TestCase
from django.contrib.auth.models import User, Group
from main.models import Empresa, Videojuego
from rest_framework.test import APIClient

class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_user(username='admin', password='admin123')
        self.basic_user = User.objects.create_user(username='usuario', password='usuario123')

        admin_group = Group.objects.get(name='administradores')
        user_group = Group.objects.get(name='usuarios')

        self.admin_user.groups.add(admin_group)
        self.basic_user.groups.add(user_group)

        self.empresa = Empresa.objects.create(nombre='Empresa1', descripcion='Descripcion1')
        self.videojuego = Videojuego.objects.create(nombre='Videojuego1', empresa=self.empresa, descripcion='Descripcion del Videojuego')

    def test_admin_can_create_empresa(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.post('/api/empresas/', {'nombre': 'Empresa2', 'descripcion': 'Descripcion2'})
        self.assertEqual(response.status_code, 201)

    def test_user_cannot_delete_empresa(self):
        self.client.login(username='usuario', password='usuario123')
        response = self.client.delete(f'/api/empresas/{self.empresa.id}/')
        self.assertEqual(response.status_code, 403)
