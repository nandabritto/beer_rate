from django.http import Http404
from django.shortcuts import render, get_object_or_404, render
from .models import BeerReview, Beer
from .forms import Beer_Review_Form, Create_BeerStyle_Form, Create_Beer_Form
from .models import BeerStyle
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView
from django.views import generic



class HomeView(ListView):
    model = BeerReview
    template_name = 'home.html'

class AddReviewView(View):
    template_name = 'add_review.html'

    def get_object(self):
        try:
            obj = BeerReview.objects.all()
        except BeerReview.DoesNotExist:
            raise Http404('Beer Review not found!')
        return obj

    def get_context_data(self, **kwargs):
        kwargs['review'] = self.get_object()
        
        if 'review_form' not in kwargs:
            kwargs['review_form'] = Beer_Review_Form()
        if 'style_form' not in kwargs:
            kwargs['style_form'] = Create_BeerStyle_Form()
        if 'beer_form' not in kwargs:
            kwargs['beer_form'] = Create_Beer_Form()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'review' in request.POST:
            review_form = Beer_Review_Form(request.POST)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user_name = request.user
                review.save()
                                                
            else:
                ctxt['review_form'] = review_form

        elif 'beer_style' in request.POST:
            style_form = Create_BeerStyle_Form(request.POST)

            if style_form.is_valid():
                style_form.save()
            else:
                ctxt['style_form'] = style_form

        elif 'beer_name' in request.POST:
            beer_form = Create_Beer_Form(request.POST)

            if beer_form.is_valid():
                beer_form.save()
            else:
                ctxt['beer_form'] = beer_form

   
        return render(request, self.template_name, self.get_context_data(**ctxt))


class BeerRatingView(ListView):
    model = BeerReview
    template_name = 'review_list.html'

class BeerStyleCreateView(ListView):
    template_name = 'add_review/create_style.html'
    form_class = Create_BeerStyle_Form
    success_message = 'Success: Beer Style was created.'

class ReviewDetailView(DetailView):
    model = BeerReview
    template_name = 'review_list/review_detail.html'
