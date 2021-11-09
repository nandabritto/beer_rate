from django.urls import path
from .views import HomeView, BeerRatingView, AddReviewView, \
    ReviewDetailView, UpdateReviewView, DeleteReviewView, \
    style_category_view, beer_category_view
from . import views

urlpatterns = [
    path('home', HomeView.as_view(), name="home"),
    path('add_review/', AddReviewView.as_view(), name='add_review'),
    path('review_list/', BeerRatingView.as_view(), name='review_list'),
    path('review_list/review_detail/<int:pk>',
         ReviewDetailView.as_view(), name='review_detail'),
    path('review_list/edit/<int:pk>',
         UpdateReviewView.as_view(), name='review_update'),
    path('review_list/delete/<int:pk>',
         DeleteReviewView.as_view(), name='review_delete'),
    path('review_list/category/<str:style>',
         style_category_view, name='category'),
    path('review_list/category',
         views.beer_category_view, name='beercategory'),
     
]
