from django import forms
from .models import BeerReview, BeerStyle
from bootstrap_modal_forms.forms import BSModalModelForm


class Beer_Review_Form(forms.ModelForm):
    class Meta:
        model = BeerReview
        fields = ['beer_style', 'beer', 'review','bitterness', 'user_name' , 'money_value', 'beer_image']

        widgets = {
            # 'beer_style' : forms.TextInput(attrs={'class':'col-form-label'}),
            # 'beer' : forms.TextInput(attrs={'class':'col-form-label'}),
            'review' : forms.Textarea(attrs={'class':'form-control'}),
            # 'bitterness' : forms.Select(),
            # 'money_value' : forms.Select(),
        }

class Create_BeerStyle_Form(BSModalModelForm):
    class Meta:
        model = BeerStyle
        fields = '__all__'