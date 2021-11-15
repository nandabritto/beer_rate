
from django.test import TestCase
from django.contrib.auth.models import User

from .models import BeerStyle, Beer, BeerReview
from django.urls import reverse

import logging


class SetupModelTestCase(TestCase):
    '''Base test case to be used in all models tests'''
    def setUp(self):
        self.username = 'joe'
        self.password = '12345'
        user = User.objects.create_user(
            username=self.username,
            email='joe@doe.com',
            password=self.password)
        self.client.login(username='joe', password='12345')
        self.beer = Beer.objects.create(beer_name='Beer')
        self.beer_style = BeerStyle.objects.create(beer_style='Style')
        self.beer_review = BeerReview.objects.create(
            beer_style=self.beer_style,
            beer=self.beer,
            user_name=user,
            pub_date='Oct. 24, 2021, 8:52 p.m.',
            review='Review Test',
            bitterness='5',
            money_value='3',
            score='1')
        

class BeerStyleTestCase(SetupModelTestCase):

    def test_absolute_url(self):
        # logging.debug(self.beer_style)
        self.assertEqual(self.beer_style.get_absolute_url(), reverse('add_review'))

class BeerTestCase(SetupModelTestCase):

    def test_absolute_url(self):
        # logging.debug(self.beer)
        self.assertEqual(self.beer.get_absolute_url(), reverse('add_review'))

class BeerReviewTestCase(SetupModelTestCase):

    def test__str__(self):
        # logging.debug(str(self.beer.beer_name))
        beerreview = BeerReview.objects.get(pk=1)
        self.assertEqual(str(beerreview.beer), self.beer.beer_name.lower())
        # self.assertEqual(self.beer.beer_name, self.beer.beer_name.lower())

    def test_absolute_url(self):
        # logging.debug(self.beer_review.id)
        self.assertEqual(self.beer_review.get_absolute_url(), reverse('review_detail', kwargs={'pk':self.beer_review.id}))
