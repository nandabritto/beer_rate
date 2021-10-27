from django.urls import path, include
from .views import HomeView, BeerRatingView, AddReviewView, ReviewDetailView, UpdateReviewView



urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    # path('rate/<int:pk>', BeerRatingView.as_view(), name='beer-rate'),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    path('review_list/', BeerRatingView.as_view(), name='review_list'),
    path('review_list/review_detail/<int:pk>', ReviewDetailView.as_view(), name='review_detail'),
    path('review_list/edit/<int:pk>', UpdateReviewView.as_view(), name='update_review'),

]
