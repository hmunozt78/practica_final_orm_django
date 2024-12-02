from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre="Laboratorio1", ciudad="Santiago", pais="Chile")

    def test_laboratorio_data(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio1")

    def test_url_status_code(self):
        response = self.client.get(reverse('laboratorios'))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse('laboratorios'))
        self.assertTemplateUsed(response, 'laboratorio/laboratorios.html')
