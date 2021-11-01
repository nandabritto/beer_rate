from django.test import TestCase
from .models import Beer
from .forms import Create_Beer_Form


class Setup_Class(TestCase):
    def set_up(self):
        self.beer = Beer.objects.create(beer_name='nametest')
        # self.style = Beer.objects.create(style='beer style test')


class Create_Beer_Form_Test(TestCase):

    def test_Create_Beer_Form_valid(self):
        
        form = Create_Beer_Form(data={
            "beer_name" : "nametest1"
        })
        self.assertTrue(form.is_valid())

    def test_Create_Beer_Form_invalid(self):
        
        form = Create_Beer_Form(data={
            "beer_name" : ""
        })
        self.assertFalse(form.is_valid())

    def test_Create_Beer_Form_lenght(self):
        
        form = Create_Beer_Form(data={
            "beer_name" : str('a'*300)
        })
        self.assertFalse(form.is_valid())
