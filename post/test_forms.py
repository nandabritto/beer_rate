from django.test import TestCase
from .models import Beer
from .forms import CreateBeerForm, CreateBeerStyleForm, BeerReviewForm
from unittest import mock


# class Setup_Class(TestCase):
    # def set_up(self):
    #     beer = Beer.objects.create(beer_name='nametest')
    #     self.beer_style = Beer_Style.objects.create(beer_style='styletest')
    #     self.review = BeerReview.objects.create(review='Review Test')
    #     self.bitterness = BeerReview.objects.create(bitterness='5')
    #     self.money_value = BeerReview.objects.create(money_value='2')
    #     self.score = BeerReview.objects.create(score='5')
    #     self.pub_date = BeerReview.objects.create(pub_date='Oct. 31, 2021, 2:24 p.m. ')
    #     self.user_name = BeerReview.objects.create(usr_name='Fernanda')


class CreateBeerForm_Test(TestCase):

    def test_CreateBeerForm_valid(self):
        # Valid beer form
        form = CreateBeerForm(data={
            "beer_name": "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_CreateBeerForm_invalid(self):
        # Invalid beer form - beer_name empty
        form = CreateBeerForm(data={
            "beer_name": ""
        })
        self.assertFalse(form.is_valid())

    def test_CreateBeerForm_lenght(self):
        # Invalid beer form beer_name too long
        form = CreateBeerForm(data={
            "beer_name": str('a'*300)
        })
        self.assertFalse(form.is_valid())

class Create_Beer_Style_Form_Test(TestCase):

    def test_CreateBeerStyleForm_valid(self):
        # Valid beer style form
        form = CreateBeerStyleForm(data={
            "beer_style": "styletest"
        })
        self.assertTrue(form.is_valid())

    def test_CreateBeerStyle_Form_invalid(self):
        # Invalid beer style form
        form = CreateBeerStyleForm(data={
            "beer_style": ""
        })
        self.assertFalse(form.is_valid())


