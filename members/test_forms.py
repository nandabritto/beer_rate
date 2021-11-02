from django.test import TestCase
from .forms import SignUpForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Setup_Class(TestCase):
     def setUp(self):
        username = User.objects.create(
            username="fernanda",
            password1="12345",
            password2="12345",
            email="fernandabrito@gmail.com")
       

class Create_SignUpForm_Test(TestCase):

    def test_SignUpForm_valid(self):
     # Sign Up form is valid 
        form = SignUpForm(data={
            "username":"fernanda",
            "password1":"12345",
            "password2":"12345",
            "email":"fernandabrito@gmail.com"
        })
        self.assertTrue(form.is_valid())

    def test_SignUpForm_password_invalid(self):
    # Sign Up form has invalid password
        form = SignUpForm(data={
            "username":"fernanda",
            "password1":"12345",
            "password2":"54321",
            "email":"fernandabrito@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_SignUpForm_username_empty(self):
        # Sign Up form has username empty
        form = SignUpForm(data={
            "username":"",
            "password1":"12345",
            "password2":"12345",
            "email":"fernandabrito@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_SignUpForm_email_invalid(self):
        # Sign Up form has username empty
        form = SignUpForm(data={
            "username":"fernanda",
            "password1":"12345",
            "password2":"12345",
            "email":"fernandabrito.gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_SignUpForm_clean_username_is_lower(self):
        # Sign Up form is valid 
        form = SignUpForm(data={
            "username":"FERNANDAA",
            "password1":"12345",
            "password2":"12345",
            "email":"fernandabrito@gmail.com"
        })
        self.assertTrue(form.is_valid())
        form.save()
        username = User.objects.get(username="fernandaa") 
        self.assertEqual(str(username.username), "fernandaa")

# https://goodcode.io/articles/django-assert-raises-validationerror/
    # def test_SignUpForm_clean_username_is_diplicated(self):
    #     # Sign Up form is valid 
    #     form = SignUpForm(data={
    #         "username":"fernanda",
    #         "password1":"12345",
    #         "password2":"12345",
    #         "email":"fernandabrito@gmail.com"
    #     })
    #     self.assertTrue(form.is_valid())
    #     username = form.save()
    #     self.assertEqual(str(username.username), "fernanda")
    #     self.assertRaises(ValidationError, form.save(), username=="fernanda")

