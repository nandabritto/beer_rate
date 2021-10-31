from django import forms
from .models import BeerReview, BeerStyle, Beer
from bootstrap_modal_forms.forms import BSModalModelForm


class Beer_Review_Form(forms.ModelForm):
    class Meta:
        model = BeerReview
        fields = ['beer_style', 'beer', 'review','bitterness',  'money_value', 'beer_image', 'score']

        widgets = {
            'review' : forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write your review here!'}),
        }

class Create_BeerStyle_Form(forms.ModelForm):
    class Meta:
        model = BeerStyle
        fields = ['beer_style']

        widgets = {
            'beer_style' : forms.TextInput(attrs={'class':'form-control'}),
            
        }


class Create_Beer_Form(forms.ModelForm):
    class Meta:
        model = Beer
        fields = ['beer_name']

        widgets = {
            'beer_name' : forms.TextInput(attrs={'class':'form-control'}),
        }
    