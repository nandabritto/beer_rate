"""System module"""
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .forms import SignUpForm


class CreateSignUpFormTest(TestCase):
    """ Test sign up form """
    def test_signupform_valid(self):
        """ Sign Up form is valid """
        form = SignUpForm(data={
            "username": "fernanda",
            "password1": "12345",
            "password2": "12345",
            "email": "fernandabrito@gmail.com"
        })
        self.assertTrue(form.is_valid())

    def test_signupform_password_invalid(self):
        """ Sign Up form has invalid password """
        form = SignUpForm(data={
            "username": "fernanda",
            "password1": "12345",
            "password2": "54321",
            "email": "fernandabrito@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_signupform_username_empty(self):
        """ Sign Up form has username empty"""
        form = SignUpForm(data={
            "username": "",
            "password1": "12345",
            "password2": "12345",
            "email": "fernandabrito@gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_signupform_email_invalid(self):
        """ Sign Up form has email invalid """
        form = SignUpForm(data={
            "username": "fernanda",
            "password1": "12345",
            "password2": "12345",
            "email": "fernandabrito.gmail.com"
        })
        self.assertFalse(form.is_valid())

    def test_signupform_clean_username_is_lower(self):
        """ Test if sign Up form username is lower """
        form = SignUpForm(data={
            "username": "FERNANDAA",
            "password1": "12345",
            "password2": "12345",
            "email": "fernandabrito@gmail.com"
        })
        self.assertTrue(form.is_valid())
        form.save()
        username = User.objects.get(username="fernandaa")
        self.assertEqual(str(username.username), "fernandaa")


class SetupClassRegisterForm(TestCase):
    """ Setup register """
    def setUp(self):
        self.user = User.objects.create(
            username="fernanda",
            password="12345",
            email="fernandabrito@gmail.com")


class CreateSignUpFormTestInvalid(SetupClassRegisterForm):
    """ Test if any field from register is duplicated or invalid """
    def test_signupform_clean_username_is_duplicated(self):
        """ Test if username is duplicated """
        form = SignUpForm(data={
            "username": "fernanda",
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(str(self.user.username), "fernanda")
        self.assertRaises(ValidationError)

    def test_signupform_clean_email_is_duplicated(self):
        """ Test if email is duplicated """
        form = SignUpForm(data={
            "email": "fernandabrito@gmail.com"
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)

    def test_signupform_clean_passwords_not_match(self):
        """ Test if passwords are not equal """
        form = SignUpForm(data={
            "password1": "1234567",
            "password2": "123456"
        })
        self.assertFalse(form.is_valid())
        self.assertRaises(ValidationError)
