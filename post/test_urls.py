'''System module'''
from django.test import TestCase


class TestUrls(TestCase):
    '''Test if urls are loading correctly'''

    def test_home_view_is_resolved(self):
        ''' Test if home view load without errors'''
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)

    def test_add_review_view_is_resolved(self):
        ''' Test if add review page load without errors'''
        response = self.client.get('/add_review')
        self.assertEqual(response.status_code, 301)

    def test_beer_rating_view_is_resolved(self):
        ''' Test if rating view load without errors'''
        response = self.client.get('/review_list')
        self.assertEqual(response.status_code, 301)
