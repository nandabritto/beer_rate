""" System Module """
from django.contrib import admin
from .models import BeerStyle, Beer, BeerReview


class BeerReviewAdmin(admin.ModelAdmin):
    """ Creates admin panel to beer_review """
    model = BeerReview
    list_display = ('beer_style', 'beer', 'user_name', 'review', 'pub_date',)
    list_filter = ['pub_date', 'user_name']
    search_fields = ['review']


admin.site.register(BeerStyle)
admin.site.register(Beer)
admin.site.register(BeerReview)
