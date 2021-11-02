from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .views import AddReviewView, ReviewDetailView
from .models import BeerReview, Beer, BeerStyle


# class AddReviewViewTest0(TestCase):
#     def test_environment_set_in_context_review(self):
#         request = RequestFactory().get('/add_review')
#         view = AddReviewView()
#         view.setup(request)

#         context = view.get_context_data()
#         self.assertIn('review', context)


#     def test_environment_set_in_context_(self):
#         request = RequestFactory().get('/add_review')
#         view = AddReviewView()
#         view.setup(request)

#         context = view.get_context_data()
#         self.assertIn('review', context)


class BeerRatingView(TestCase):
      
    def test_beer_rating_view_success_status_code(self):
        url = reverse('review_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_beer_rating_view_url_by_name(self):
        response = self.client.get(reverse('review_list'))
        self.assertEquals(response.status_code, 200)

    
    def test_beer_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('review_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_beer_rating_view_contains_correct_html(self):
        response = self.client.get(reverse('review_list'))
        self.assertContains(response, '<h3> Beer reviews </h3>')

    def test_beer_rating_view_does_not_contain_incorrect_html(self):
            response = self.client.get(reverse('review_list'))
            self.assertNotContains(
                response, 'Hi there! I should not be on the page.')


class BeerStyleCreateView(TestCase):
      
    def test_beer_rating_view_success_status_code(self):
        url = reverse('add_review')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_beer_rating_view_url_by_name(self):
        response = self.client.get(reverse('add_review'))
        self.assertEquals(response.status_code, 200)

    
    def test_beer_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('add_review'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')

    # def test_beer_rating_view_contains_correct_html(self):
    #     response = self.client.get(reverse('add_review/create_style.html'))
    #     self.assertContains(response, ' <h5>Create new Style</h5>')

    def test_beer_rating_view_does_not_contain_incorrect_html(self):
            response = self.client.get(reverse('add_review'))
            self.assertNotContains(
                response, 'Hi there! I should not be on the page.')



class ReviewDetailViewTests(TestCase):
    
    def setUp(self):
        user = User.objects.create(username="joe", password="12345")
        beer = Beer.objects.create(beer_name='Beer')
        beer_style = BeerStyle.objects.create(beer_style='Style')

        self.BeerReview =  BeerReview.objects.create(
            beer_style=beer_style,
            beer=beer,
            user_name=user,
            pub_date='Oct. 24, 2021, 8:52 p.m.',
            review='Review Test',
            bitterness='5',
            money_value='3',
            score='1')

    def test_review_detail_view_success_status_code(self):
        url = reverse('review_detail', kwargs={'pk': self.BeerReview.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_view_url_by_name(self):
        response = self.client.get(reverse('review_detail', kwargs={'pk': self.BeerReview.id}))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('review_detail', kwargs={'pk': self.BeerReview.id}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_detail.html')

    def test_add_beer_rate_contains_correct_html(self):
        response = self.client.get(reverse('review_detail', kwargs={'pk': self.BeerReview.id}))
        self.assertContains(response, 'Bitterness')

    def test_beer_rate__page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('review_detail', kwargs={'pk': self.BeerReview.id}))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')