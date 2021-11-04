from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import redirect 
from django.urls import reverse



class test_login(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='fernanda', email='fernanda@gmail.com', password='12345')

    def test_user_can_login(self):
        response = self.client.post(reverse('login'), {"username": "fernanda", "password": "12345"})
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
           
    def test_user_cannot_login(self):
        response = self.client.post(reverse('login'), {"username": "", "password": "12345"})
        self.assertRedirects(response, '/members/login_user', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)
        
    def test_user_is_not_None(self):
        response = self.client.post(reverse('login'), {"username": "", "password": "12345"})
        if self.user.username is None:
            raise ValidationError("You must have a username")


class test_logout(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='fernanda', email='fernanda@gmail.com', password='12345')

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/', status_code=302)


class test_register(TestCase):

    def test_register__user(self):
        response = self.client.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password
        })
    self.assertEqual(response.status_code, 200)

    users = get_user_model().objects.all()
    self.assertEqual(users.count(), 1)
