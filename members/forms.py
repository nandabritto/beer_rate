"""System module"""
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class SignUpForm(forms.Form):
    """Create a signup form"""
    username = forms.CharField(
        label='Enter Username',
        min_length=4,
        max_length=150)
    email = forms.EmailField(
        label='Enter Email')
    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput,)
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'})

    def clean_username(self):
        """Clean username field after form creation"""
        username = self.cleaned_data['username']
        filterusername = User.objects.filter(username=username)
        if filterusername.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        """Clean email field after form creation"""
        email = self.cleaned_data['email']
        filteremail = User.objects.filter(email=email)
        if filteremail.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        """Clean confirm password field after form creation"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self):
        """Save register form if all information is valid"""
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
