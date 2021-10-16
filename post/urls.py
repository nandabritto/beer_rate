from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('add_review', views.add_review, name = "add_review"),
    path('reviews_list/pk:<review_id>', views.review_detail, name='review_detail'),
    path('beer', views.beer_list, name='beer_list'),
    path('beer/pk:<beer_id>', views.beer_detail, name='beer_detail'),

]