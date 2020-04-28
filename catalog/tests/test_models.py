from django.test import TestCase
import os
from catalog.models import Producer, Film, Genre


class ProducerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Producer.objects.create(name='nn', biography='bb')

    def test_name(self):
        producer = Producer.objects.get(id = 1)
        field = producer._meta.get_field('name').verbose_name
        self.assertEquals(field, 'name')

    def test_biography(self):
        producer = Producer.objects.get(id = 1)
        field = producer._meta.get_field('biography').verbose_name
        self.assertEquals(field, 'biography')
