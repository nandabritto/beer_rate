from django.urls import path
from .views import HomeView, BeerRatingView, AddReviewView

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('rate/<int:pk>', BeerRatingView.as_view(), name='beer-rate'),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    path('review_list/', BeerRatingView.as_view(), name='review_list'),
 

]