from django.test import TestCase
from .models import Beer
from .forms import Create_Beer_Form, Create_BeerStyle_Form


class Setup_Class(TestCase):
    def set_up(self):
        self.beer = Beer.objects.create(beer_name='nametest')
        self.beer_style = Beer_Style.objects.create(beer_style='styletest')


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