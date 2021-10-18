from django.urls import path
from .views import HomeView, BeerRatingView, AddReviewView 

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('rate/<int:pk>', BeerRatingView.as_view(), name='beer-rate'),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    # path('reviews_list/pk:<review_id>', views.review_detail, name='review_detail'),
    # path('beer', views.beer_list, name='beer_list'),
    # path('beer/pk:<beer_id>', views.beer_detail, name='beer_detail'),

]