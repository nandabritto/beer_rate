'''System Module '''
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class TestRegister(TestCase):
    ''' Test Register Function '''

    def test_register_user(self):
        ''' Teste redirection when user register '''
        response = self.client.post(reverse('register'), data={
            'username': 'FernandaB',
            'email': 'fernandab@gmail.com',
            'password1': '123456',
            'password2': '123456'
        })
        self.assertEqual(response.status_code, 302)

    def test_register_user_invalid(self):
        ''' Test redirect if user is invalid '''
        response = self.client.post(reverse('register'), data={
            'username': 'FernandaB',
            'email': 'fernandab@gmail.com',
            'password1': '1234567',
            'password2': '123456'
        })
        self.assertEqual(response.status_code, 200)
        
    def test_register_user_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)


class TestLogin(TestCase):
    ''' Test Log In Function '''
    def setUp(self):
        ''' Setup to test login '''
        self.user = User.objects.create_user(
            username='fernanda',
            email='fernanda@gmail.com',
            password='12345')

    def test_user_can_login(self):
        ''' Test redirection if user log in '''
        response = self.client.post(reverse(
            'login'), {
            "username": "fernanda",
            "password": "12345"})
        self.assertRedirects(
            response, '/',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)

    def test_user_cannot_login(self):
        ''' Test redirection if user cannot log in '''

        response = self.client.post(reverse(
            'login'), {
            "username": "",
            "password": "12345"})
        self.assertRedirects(
            response,
            '/members/login_user',
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True)


class TestLogout(TestCase):
    ''' Test Log out Function '''
    def setUp(self):
        ''' Setup to test logout '''
        self.user = User.objects.create_user(
            username='fernanda',
            email='fernanda@gmail.com',
            password='12345')

    def test_logout(self):
        ''' Test redirection if user logout '''
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/', status_code=302)
