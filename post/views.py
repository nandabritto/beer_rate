from django.shortcuts import render, get_object_or_404, render
from .models import BeerReview, Beer
from .forms import Beer_Review_Form
from django.views.generic import ListView, DetailView, CreateView



class HomeView(ListView):
    model = BeerReview
    template_name = 'home.html'


class AddReviewView(CreateView):
    model = BeerReview
    template_name = 'add_review.html'
    fields = '__all__'
    def get_absolute_url(self):
        return reverse('home')


    
class BeerRatingView(DetailView):
    model = BeerReview
    queryset = BeerReview.objects.order_by("-pub_date")
    template_name = 'review_list.html'


# def add_review(request):
#     form = Beer_Review_Form(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form' : form
#     }

#     return render(request, 'add_review.html', context)




# def review_list(request):
#     review_list = BeerReview.objects.order_by('-pub_date')[:9]
#     context = {'review_list':review_list}
#     return render(request, 'review_list.html', context)


# def review_detail(request, review_id):
#     review = get_object_or_404(BeerReview, pk=review_id)
#     return render(request, 'reviews/review_list.html', {'review': review})


# def beer_list(request):
#     beer_list = Beer.objects.order_by('-name')
#     context = {'beer_list':beer_list}
#     return render(request, 'reviews/beer_list.html', context)


# def beer_detail(request, beer_id):
#     beer = get_object_or_404(Beer, pk=wine_id)
#     return render(request, 'reviews/beer_detail.html', {'beer': beer})
