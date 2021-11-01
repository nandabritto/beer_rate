from django.test import TestCase
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your tests here.

class Setup_Class(TestCase):
     def setUp(self):
        username = User.objects.create(
            username="fernanda",
            password1="Banana!98421",
            password2="Banana!98421",
            email="fernandabrito@gmail.com")
       

class Create_SignUpForm_Test(TestCase):

    def test_SignUpForm_valid(self):
     
        form = SignUpForm(data={
            "username":"fernanda",
            "password1":"Banana!98421",
            "password2":"Banana!98421",
            "email":"fernandabrito@gmail.com"
        })
        self.assertTrue(form.is_valid())


