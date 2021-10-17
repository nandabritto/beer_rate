from django import forms
from .models import BeerReview


class Beer_Review_Form(forms.ModelForm):
    class Meta:
        model = BeerReview
        fields = ['beer_style', 'beer', 'user_name', 'review','bitterness', 'money_value']

# form = BeerReview()
# beer_review = BeerReview.objects.get(pk=1)
# form = Beer_Review_Form(instance=beer_review)