from django.test import TestCase


class TestUrls(TestCase):
    '''Test if urls are loading correctly'''

    def test_home_is_resolved(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_add_review_is_resolved(self):
        response = self.client.get('/add_review')
        self.assertEquals(response.status_code, 200)

    def test_add_rate_url_is_resolved(self):
        pass
