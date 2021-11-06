import logging
from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, \
    View, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BeerReview
from .forms import BeerReviewForm, CreateBeerStyleForm, CreateBeerForm


class HomeView(ListView):
    '''Render homepage view '''
    model = BeerReview
    template_name = 'home.html'


class AddReviewView(View):
    '''Render add review page'''
    template_name = 'add_review.html'

    def get_object(self):
        obj = BeerReview.objects.all()       

    def get_context_data(self, **kwargs):
        '''Get the right form according to the part of the page clicked'''

        kwargs['review'] = self.get_object()
        if 'review_form' not in kwargs:
            kwargs['review_form'] = BeerReviewForm()
        if 'style_form' not in kwargs:
            kwargs['style_form'] = CreateBeerStyleForm()
        if 'beer_form' not in kwargs:
            kwargs['beer_form'] = CreateBeerForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        '''Return to add form page after creating a beer or beer style '''
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ''' Validate and create data from forms on add review page'''

        ctxt = {}

        if 'review' in request.POST:
            review_form = BeerReviewForm(request.POST)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user_name = request.user
                review.save()
                return redirect('review_detail',review.pk)

            else:
                ctxt['review_form'] = review_form

        elif 'beer_style' in request.POST:
            style_form = CreateBeerStyleForm(request.POST)

            if style_form.is_valid():
                style_form.save()
            else:
                ctxt['style_form'] = style_form

        elif 'beer_name' in request.POST:
            beer_form = CreateBeerForm(request.POST)

            if beer_form.is_valid():
                beer_form.save()
            else:
                ctxt['beer_form'] = beer_form

        return render(
            request, self.template_name, self.get_context_data(**ctxt))


class BeerRatingView(ListView):
    '''Creates a list view of all reviews on website'''
    model = BeerReview
    template_name = 'review_list.html'
    paginate_by = 6
    ordering = ['pub_date']


class BeerStyleCreateView(ListView):
    '''Create a beer style on add review page'''
    template_name = 'add_review/create_style.html'
    form_class = CreateBeerStyleForm
    # success_message = 'Success: Beer Style was created.'


class ReviewDetailView(DetailView):
    '''Create a detailed view of every review on website'''
    model = BeerReview
    template_name = 'review_list/review_detail.html'


class UpdateReviewView(UpdateView):
    '''Update a review after editing'''
    model = BeerReview
    form_class = BeerReviewForm
    template_name = 'review_list/review_update.html'

    def form_valid(self, form):
        '''validate update review form and save it'''
    
        self.object = form.save(commit=False)
        self.object.save()
        return redirect('review_detail', self.object.pk)
    





class DeleteReviewView(DeleteView):
    '''Delete a beer review form'''
    model = BeerReview
    form_class = BeerReviewForm
    template_name = 'review_list/review_delete.html'
    success_url = reverse_lazy('review_list')
