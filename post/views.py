from django.shortcuts import render, get_object_or_404, render
from .models import BeerReview, Beer

def home(request):
    return render(request, 'home.html', {})

def add_review(request):
    return render(request, 'add_review.html', {})

def review_list(request):
    review_list = BeerReview.objects.order_by('-pub_date')[:9]
    context = {'review_list':review_list}
    return render(request, 'review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(BeerReview, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def beer_list(request):
    beer_list = Beer.objects.order_by('-name')
    context = {'beer_list':beer_list}
    return render(request, 'reviews/beer_list.html', context)


def beer_detail(request, beer_id):
    beer = get_object_or_404(Beer, pk=wine_id)
    return render(request, 'reviews/beer_detail.html', {'beer': beer})