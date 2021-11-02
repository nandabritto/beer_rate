from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import redirect 



class Testlogin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='fernanda', email='fernanda@gmail.com', password='12345')

    def test_user_can_login(self):
        response = self.client.post("/login", {"username": "fernanda", "password": "12345"})
        return redirect('home')
        
    def test_user_is_not_None(self):
        response = self.client.post("/login", {"username": "", "password": "12345"})
        if self.user.username is None:
            raise ValidationError("You must have a username")
