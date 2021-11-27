""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from post.models import BeerReview, Beer, BeerStyle


class SetupViewTestCase(TestCase):
    """ Base test """
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
        self.url = reverse('review_update', kwargs={
            'pk': 1
        })


class TestHttpErrors(SetupViewTestCase):
    """ Test raised errors pages """
    def setUp(self):
        """Setup user and review from SetupViewTestCase"""
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)

    def test_page_not_found_view(self):
        """ Test if review detail url exist """
        response = self.client.get(
            '/review_list/review_detail/0')
        self.assertEqual(response.status_code, 404)

    # def test_my_custom_permission_denied_view(self):
    #     super().__init__()
    #     self.client.login(username='joana', password='12345')
    #     response = self.client.get(
    #         'review_list/edit')
    #     self.assertEqual(response.status_code, 403)
