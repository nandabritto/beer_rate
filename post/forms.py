""" System module """
from django import forms
from .models import BeerReview, BeerStyle, Beer


class BeerReviewForm(forms.ModelForm):
    """ Create a BeerReview Form """
    class Meta:
        """Get beer review model, choose fields to display and add widgets
        with bootstrap classes"""
        model = BeerReview
        fields = [
            'beer_style',
            'beer',
            'review',
            'bitterness',
            'money_value',
            'beer_image',
            'score']
        widgets = {
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here!'}),
                }


class CreateBeerStyleForm(forms.ModelForm):
    """ Create a BeerStyle Form """
    class Meta:
        """Get beer model, choose field to display and add widget
        with bootstrap class"""
        model = BeerStyle
        fields = ['beer_style']
        widgets = {
            'beer_style': forms.TextInput(attrs={
                'class': 'form-control'}),
        }


class CreateBeerForm(forms.ModelForm):
    """ Create a Beer Form """
    class Meta:
        """Get beer style model, choose field to display and add widget
        with bootstrap classes"""
        model = Beer
        fields = ['beer_name']
        widgets = {
            'beer_name': forms.TextInput(attrs={
                'class': 'form-control'}),
        }
