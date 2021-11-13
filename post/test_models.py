
from django.test import TestCase
from .models import BeerStyle, Beer
from django.urls import reverse

import logging

class SetupModelTestCase(TestCase):
    '''Base test case to be used in all PostUpdateView view tests'''
    def setUp(self):
        self.beer = Beer.objects.create(beer_name='Beer')
        self.beer_style = BeerStyle.objects.create(beer_style='Style')

class BeerStyleTestCase(SetupModelTestCase):

    def test_absolute_url(self):
        logging.debug(self.beer_style)
        self.assertEqual(self.beer_style.get_absolute_url(), reverse('add_review'))