from django.test import TestCase
from .models import BeerReview


class TestUrls(TestCase):
    '''Test if urls are loading correctly'''

    def setup(TestCase):
        self.review = ReviewBeer.objects.create(
            beer_name= "nametest1",
            beer_style= "styletest",
            review= "Review Test",
            bitterness= "5",
            money_value="2",
            score="5",
            user_name="Fernanda")

    def test_HomeView_is_resolved(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_AddReviewView_is_resolved(self):
        response = self.client.get('/add_review')
        self.assertEquals(response.status_code, 301)

    def test_BeerRatingView_is_resolved(self):
        response = self.client.get('/review_list')
        self.assertEquals(response.status_code, 301)

    def test_ReviewDetailView_is_resolved(self):
        response = self.client.get('/review_detail')
        self.assertEquals(response.status_code, 200)
