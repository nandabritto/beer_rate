from django.test import RequestFactory, TestCase
from django.urls import reverse
from .views import AddReviewView


# class AddReviewViewTest(TestCase):
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