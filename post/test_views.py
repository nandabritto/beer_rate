'''System module'''
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import BeerReview, Beer, BeerStyle


class SetupViewTestCase(TestCase):
    '''Base test case to be used in all PostUpdateView view tests'''
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
            'pk': self.beer_review.id
        })


class BeerRatingView(SetupViewTestCase):
    '''Test Beer rating view response, correct url and template'''
    def test_beer_rating_view_success_status_code(self):
        ''' Test response on review list page by url'''
        url = reverse('review_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_beer_rating_view_url_by_name(self):
        ''' Test response on review list page by name'''
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)

    def test_beer_rating_view_uses_correct_template(self):
        ''' Test if review list is rendering correct template'''
        response = self.client.get(reverse('review_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list.html')

    def test_beer_rating_view_contains_correct_html(self):
        ''' Test if review list is rendering correct html'''
        response = self.client.get(reverse('review_list'))
        self.assertContains(response, ' Beer reviews')

    def test_beer_rating_view_does_not_contain_incorrect_html(self):
        ''' Test if review list is rendering incorrect html and
        display a message'''
        response = self.client.get(reverse('review_list'))
        self.assertNotContains(
                response, 'Hi there! I should not be on the page.')


class BeerStyleCreateView(SetupViewTestCase):
    '''Test Beer Style view response, correct url and template'''
    def test_beer_style_view_success_status_code(self):
        ''' Test response on beer style modal view by url'''
        url = reverse('add_review')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_beer_style_view_url_by_name(self):
        ''' Test response on beer style modal by name'''
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)

    def test_beer_style_view_uses_correct_template(self):
        ''' Test response on beer style modal is using correct
        template'''
        response = self.client.get(reverse('add_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_review.html')

    def test_beer_style_view_does_not_contain_incorrect_html(self):
        ''' Test response on beer style modal is using incorrect template
        and shows a message'''
        response = self.client.get(reverse('add_review'))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class ReviewDetailViewTests(SetupViewTestCase):
    '''Test Review Detail view response, correct url and template'''

    def test_review_detail_view_url_exists(self):
        ''' test if review detail url exist'''
        response = self.client.get(
            '/review_list/review_detail/' + str(self.beer_review.id))
        self.assertEqual(response.status_code, 200)

    def test_review_detail_view_success_status_code(self):
        '''test if review detail view render correct'''
        url = reverse('review_detail', kwargs={
            'pk': self.beer_review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_review_detail_view_url_by_name(self):
        '''test if review detail view render correct by name'''
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.beer_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_review_detail_view_uses_correct_template(self):
        '''test if detail view uses correct template'''
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.beer_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_detail.html')

    def test_rview_detail_view_contains_correct_html(self):
        '''test if review detail has correct html'''
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.beer_review.id}))
        self.assertContains(response, 'Rating')

    def test_review_detail_view_does_not_contain_incorrect_html(self):
        '''test if review detail has wrong html and displays a message'''
        response = self.client.get(reverse('review_detail', kwargs={
            'pk': self.beer_review.id}))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class AddReviewViewTest(SetupViewTestCase):
    '''Test Add review view response, correct url and template'''

    def setUp(self):
        '''Setup user and review from SetupViewTestCase'''

        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_add_review_beer_style_post(self):
        '''Login a mock user and test if add beer style is using
        correct form and post it correct'''
        super().__init__()
        self.client.login(username='testuser', password='12345')
        payload = {'beer_style': 'Style_post2'}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('style_form', response.context)

    def test_add_review_beer_style_form_invalid(self):
        '''Login a mock user and test if add beer style is using
        correct form and refresh page when beer style is empty'''
        self.client.login(username='testuser', password='12345')
        payload = {'beer_style': ''}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('style_form', response.context)

    def test_add_review_beer_name_post(self):
        '''Login a mock user and test if add beer name is using
        correct form and post it correct'''
        payload = {'beer_name': 'Beer_post'}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('beer_form', response.context)

    def test_add_review_beer_form_invalid(self):
        '''Login a mock user and test if add beer name is using
        correct form and refresh page when beer name is empty'''
        self.client.login(username='testuser', password='12345')
        payload = {'beer_name': ''}
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('beer_form', response.context)

    def test_add_review_beer_can_post(self):
        '''Create a mock user and a review, check if review is correct post
        and redirect user'''

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

    def test_add_review_form_invalid(self):
        '''Create a mock user and a review, check if review is incorrect and
        refesh the page'''
        self.client.login(username='joe', password='12345')
        payload = {
                    'beer_style': self.beer_style.id,
                    'beer': self.beer.id,
                    'review': 'Review from post method',
                    'bitterness': '',
                    'money_value': '',
                    'beer_image': '',
                    'score': '1'
                    }
        response = self.client.post(reverse('add_review'), payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn('review_form', response.context)


class PostUpdateViewTests(SetupViewTestCase):
    '''Test Upadate review view render response'''

    def setUp(self):
        '''Setup user and review from SetupViewTestCase'''
        super().setUp()
        self.client.login(user_name=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        '''Test if update view is rendering right'''
        self.assertEqual(self.response.status_code, 200)


class SuccessfulPostUpdateViewTests(SetupViewTestCase):
    '''Test Upadate review sucessfull view response'''

    def setUp(self):
        '''Setup user and review from SetupViewTestCase'''
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    def test_review_changed(self):
        '''test if update review is done correctlly and refresh db'''
        self.beer_review.review = 'Review Test edited'
        self.beer_review.save()
        self.beer_review.refresh_from_db()
        self.assertEqual(self.beer_review.review, 'Review Test edited')

    def test_review_update_url_exists(self):
        '''Test iif review update page renders correct'''
        response = self.client.get(
            '/review_list/edit/' + str(self.beer_review.id))
        self.assertEqual(response.status_code, 200)

    def test_review_update_view_success_status_code(self):
        '''Test status code from review update page'''
        url = reverse('review_update', kwargs={
            'pk': self.beer_review.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_review_update_url_by_name(self):
        '''Test if update review is getting correct url'''
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertEqual(response.status_code, 200)

    def test_review_update_uses_correct_template(self):
        '''Test if review update use correct template'''
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/review_update.html')

    def test_review_update_contains_correct_html(self):
        '''Test if review update use correct html'''
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertContains(response, 'Bitterness')

    def test_review_update__page_does_not_contain_incorrect_html(self):
        '''Test if review update use incorrect template'''
        response = self.client.get(reverse('review_update', kwargs={
            'pk': self.beer_review.id}))
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')


class TestStyleCategoryView(SetupViewTestCase):
    '''Teste category view in all pages '''
    def setUp(self):
        '''Setup user and review from SetupViewTestCase'''
        super().setUp()
        self.client.login(username=self.username, password=self.password)

    def test_style_category_view(self):
        '''Test if beer style are loading on search in all pages'''
        style = self.beer_style.beer_style
        response = self.client.get(reverse('category', kwargs={
            'style': style}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/stylecategories.html')

    def test_beer_category_view_get(self):
        '''Test if beer name are loading on search in all pages'''
        search = {'searched': self.beer.beer_name}
        response = self.client.get(reverse('beercategory'), search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/beercategories.html')

    def test_beer_category_view_post(self):
        '''Test if beer name search are posting '''
        search = {'searched': self.beer.beer_name}
        response = self.client.post(reverse('beercategory'), search)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'review_list/beercategories.html')
