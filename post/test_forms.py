from django.test import TestCase
from .models import Beer
from .forms import Create_Beer_Form, Create_BeerStyle_Form, Beer_Review_Form
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


class Create_Beer_Form_Test(TestCase):

    def test_Create_Beer_Form_valid(self):
        # Valid beer form
        form = Create_Beer_Form(data={
            "beer_name": "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_Create_Beer_Form_invalid(self):
        # Invalid beer form - beer_name empty
        form = Create_Beer_Form(data={
            "beer_name": ""
        })
        self.assertFalse(form.is_valid())

    def test_Create_Beer_Form_lenght(self):
        # Invalid beer form beer_name too long
        form = Create_Beer_Form(data={
            "beer_name": str('a'*300)
        })
        self.assertFalse(form.is_valid())

class Create_Beer_Style_Form_Test(TestCase):

    def test_Create_BeerStyle_Form_valid(self):
        # Valid beer style form
        form = Create_BeerStyle_Form(data={
            "beer_style": "styletest"
        })
        self.assertTrue(form.is_valid())

    def test_Create_BeerStyle_Form_invalid(self):
        # Invalid beer style form
        form = Create_BeerStyle_Form(data={
            "beer_style": ""
        })
        self.assertFalse(form.is_valid())


# class Create_Beer_Review_Form_Test(TestCase):

#     def test_Beer_Review_Form_valid(self):
#         form = Beer_Review_Form(data={
#             "beer_name": "nametest1",
#             "beer_style": "styletest",
#             "review": "Review Test",
#             "bitterness": "5",
#             "money_value":"2",
#             "score":"5",
#             "user_name":"Fernanda"
#         })
#         self.assertTrue(form.is_valid())
