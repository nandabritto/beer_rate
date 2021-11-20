""" System module """
from django.test import TestCase
from .forms import CreateBeerForm, CreateBeerStyleForm


class CreateBeerFormTest(TestCase):
    """ Test Create Beer Form """
    def test_createbeer_form_valid(self):
        """Test if beer form is valid"""
        form = CreateBeerForm(data={
            "beer_name": "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_createbeer_form_invalid(self):
        """ Test if Create Beer Form  is invalid
        - beer_name empty """
        form = CreateBeerForm(data={
            "beer_name": ""
        })
        self.assertFalse(form.is_valid())

    def test_createbeer_form_lenght(self):
        """ Test if Create Beer Form  is invalid
         beer_name too long """
        form = CreateBeerForm(data={
            "beer_name": str('a'*300)
        })
        self.assertFalse(form.is_valid())


class CreateBeerStyleFormTest(TestCase):
    """ Test Create Beer Style Form """
    def test_createbeerstyle_form_valid(self):
        """ Test if Create Beer Style Form  is valid """
        form = CreateBeerStyleForm(data={
            "beer_style": "styletest"
        })
        self.assertTrue(form.is_valid())

    def test_createbeerstyle_form_invalid(self):
        """ Test if Create Beer Style Form  is invalid """
        form = CreateBeerStyleForm(data={
            "beer_style": ""
        })
        self.assertFalse(form.is_valid())
