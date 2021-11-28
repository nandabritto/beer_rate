""" System Module """
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from post.models import BeerReview, Beer, BeerStyle


class TestHttpErrors(TestCase):
    """ Test raised 404 error page """
    def test_page_not_found_view(self):
        """ Test if review detail url exist """
        response = self.client.get(
            '/review_list/review_detail/0')
        self.assertEqual(response.status_code, 404)
