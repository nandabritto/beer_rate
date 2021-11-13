
from django.test import TestCase
from .models import BeerStyle
from django.urls import reverse

import logging



# class BeerStyleModelTestCase(TestCase):

    # @classmethod
    # def setup(cls):
    #     cls.beerstyle1 = BeerStyle( beer_style = 'style12')
    #     cls.beerstyle1.save()
        # return str(cls.beer_style).lower()

class BeerStyleTestCase(TestCase):

    def test_absolute_url(self):
        self.beerstyle1 = BeerStyle( beer_style = 'style12')
        self.beerstyle1.save()
        logging.debug(self.beerstyle1)
        self.assertEqual(self.beerstyle1.get_absolute_url(), reverse('add_review'))