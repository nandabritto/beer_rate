from django.test import TestCase
from django.urls import reverse, resolve 



class TestUrls(TestCase):

    def test_home_is_resolved(self):
       response = self.client.get('/')
       self.assertEquals(response.status_code, 200)
       

    def test_add_review_is_resolved(self):
       response = self.client.get('/add_review')
       self.assertEquals(response.status_code, 200)
    
    def test_add_rate_url_is_resolved(self):
        pass