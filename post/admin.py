from django.contrib import admin

from .models import BeerStyle, Beer, BeerReview

class BeerReviewAdmin(admin.ModelAdmin):
    model = BeerReview
    list_display = ('beer_style','beer', 'user_name', 'review', 'pub_date',)
    list_filter = ['pub_date', 'user_name']
    search_fields = ['review']
    
admin.site.register(BeerStyle)
admin.site.register(Beer)
admin.site.register(BeerReview, BeerReviewAdmin)
