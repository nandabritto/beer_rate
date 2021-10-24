from django.shortcuts import render, get_object_or_404, render
from .models import BeerReview, Beer
from .forms import Beer_Review_Form, Create_BeerStyle_Form
from .models import BeerStyle
from django.views.generic import ListView, DetailView, CreateView


class HomeView(ListView):
    model = BeerReview
    template_name = 'home.html'


class AddReviewView(CreateView):
    model = BeerReview
    form_class = Beer_Review_Form
    template_name = 'add_review.html'

    def get_review(request):
        if request.method == 'POST':
            
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/thanks/')

        else:
            form = form_class

        return render(request, 'home.html', {'form': form_class})


        
class BeerRatingView(ListView):
    model = BeerReview
    template_name = 'review_list.html'


class BeerStyleCreateView(ListView):
    template_name = 'add_review/create_style.html'
    form_class = Create_BeerStyle_Form
    success_message = 'Success: Beer Style was created.'
        





    
