import logging
from django.test import RequestFactory, TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import AddReviewView, UpdateReviewView
from .models import BeerReview, Beer, BeerStyle
from .forms import Beer_Review_Form


class BeerRatingView(TestCase):
    '''Test Beer rating view response, correct url and template'''
    def test_beer_rating_view_success_status_code(self):
        url = reverse('review_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_beer_rating_view_url_by_name(self):
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)

    def test_beer_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_beer_rating_view_contains_correct_html(self):
        response = self.client.get(reverse('review_list'))
        self.assertContains(response, '<h3> Beer reviews </h3>')

    def test_beer_rating_view_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('review_list'))
        self.assertNotContains(
                response, 'Hi there! I should not be on the page.')


class BeerStyleCreateView(TestCase):
    '''Test Beer Style view response, correct url and template'''
    def test_beer_rating_view_success_status_code(self):
        url = reverse('add_review')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_beer_rating_view_url_by_name(self):
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)

    def test_beer_rating_view_uses_correct_template(self):
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')

    def test_beer_rating_view_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('add_review'))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class ReviewDetailViewTests(TestCase):
    '''Test Review Detail view response, correct url and template'''
    def setUp(self):
        user = User.objects.create(username="joe", password="12345")
        beer = Beer.objects.create(beer_name='Beer')
        beer_style = BeerStyle.objects.create(beer_style='Style')

        self.BeerReview = BeerReview.objects.create(
            beer_style=beer_style,
            beer=beer,
            user_name=user,
            pub_date='Oct. 24, 2021, 8:52 p.m.',
            review='Review Test',
            bitterness='5',
            money_value='3',
            score='1')

    def test_view_url_exists(self):
        response = self.client.get(
            '/review_list/review_detail/' + str(self.BeerReview.id))
        self.assertEqual(response.status_code, 200)

    def test_review_detail_view_success_status_code(self):
        url = reverse('review_detail', kwargs={
            'pk': self.BeerReview.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.BeerReview.id}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.BeerReview.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_detail.html')

    def test_add_beer_rate_contains_correct_html(self):
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.BeerReview.id}))
        self.assertContains(response, 'Bitterness')

    def test_beer_rate__page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.BeerReview.id}))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class AddReviewViewTest(TestCase):
    '''Test Add review view response, correct url and template'''
    def setUp(self):
        self.user = User.objects.create(username="joe", password="12345")
        self.user.save()
        self.client.login(username='joe', password='12345')
        self.beer = Beer.objects.create(beer_name='Beer_Post')
        self.beer_style = BeerStyle.objects.create(beer_style='Style_post')

    def test_add_review_beer_stype_post(self):
        payload = {'beer_style': 'Style_post'}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)

    def test_add_review_beer_name_post(self):
        payload = {'beer_name': 'Beer_post'}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)

    def test_add_review_beer_review_post(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client = Client()
        self.client.login(username='testuser', password='12345')

        payload = {
                    'beer_style': self.beer_style.id,
                    'beer': self.beer.id,
                    'review': 'Review from post method',
                    'bitterness': '4',
                    'money_value': '4',
                    'beer_image': '',
                    'score': '1'
                    }
        response = self.client.post(reverse('add_review'), data=payload)
        self.assertEqual(response.status_code, 302)


class PostUpdateViewTestCase(TestCase):
    '''
    Base test case to be used in all `PostUpdateView` view tests
    '''
    def setUp(self):
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        beer = Beer.objects.create(beer_name='Beer')
        beer_style = BeerStyle.objects.create(beer_style='Style')
        self.beer_review = BeerReview.objects.create(
            beer_style=beer_style,
            beer=beer,
            user_name=user,
            pub_date='Oct. 24, 2021, 8:52 p.m.',
            review='Review Test',
            bitterness='5',
            money_value='3',
            score='1')
        self.url = reverse('review_update', kwargs={
            'pk': self.beer_review.id
        })

class PostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

  
class SuccessfulPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    # def test_redirection(self):
    #     '''
    #     A valid form submission should redirect the user
    #     '''
    #     reviews_url = reverse('review_detail', kwargs={'pk': self.beer_review.id})
    #     self.assertRedirects(self.response, reviews_url)

    def test_review_changed(self):
        self.beer_review.review = 'Review Test edited'
        self.beer_review.save()
        self.beer_review.refresh_from_db()
        self.assertEquals(self.beer_review.review, 'Review Test edited')

    def test_review_update_url_exists(self):
        response = self.client.get(
            '/review_list/edit/' + str(self.beer_review.id))
        self.assertEqual(response.status_code, 200)

    def test_review_update_view_success_status_code(self):
        url = reverse('review_update', kwargs={
            'pk': self.beer_review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_review_update_url_by_name(self):
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_review_update_uses_correct_template(self):
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_update.html')

    def test_review_update_contains_correct_html(self):
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertContains(response, 'Bitterness')

    def test_review_update__page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

