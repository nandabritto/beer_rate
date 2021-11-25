""" System module """
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import ListView, DetailView, \
    View, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import BeerReview, BeerStyle
from .forms import BeerReviewForm, CreateBeerStyleForm, CreateBeerForm


class HomeView(ListView):
    """ Render homepage view """
    model = BeerReview
    template_name = 'home.html'


class AddReviewView(View):
    """ Render add review page """
    template_name = 'add_review.html'

    def get_object(self):
        """ Get objects from BeerReview model """
        obj = BeerReview.objects.all()
        return obj

    def get_context_data(self, **kwargs):
        """ Get the right form according to the part of the page clicked """
        kwargs['review'] = self.get_object()
        if 'review_form' not in kwargs:
            kwargs['review_form'] = BeerReviewForm()
        if 'style_form' not in kwargs:
            kwargs['style_form'] = CreateBeerStyleForm()
        if 'beer_form' not in kwargs:
            kwargs['beer_form'] = CreateBeerForm()
        return kwargs

    def get(self, request):
        """ Return to add form page after creating a beer or beer style """
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        """ Validate and create data from forms on add review page """
        ctxt = {}
        if 'review' in request.POST:
            review_form = BeerReviewForm(request.POST, request.FILES)

            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user_name = request.user
                review.slug = review.beer_style
                review.save()
                return redirect('review_detail', review.pk)
            else:
                ctxt['review_form'] = review_form

        elif 'beer_style' in request.POST:
            style_form = CreateBeerStyleForm(request.POST)
            if style_form.is_valid():
                messages.success(request, f'{"Beer style has been created."}')
                style_form.save()
            else:
                ctxt['style_form'] = style_form

        elif 'beer_name' in request.POST:
            beer_form = CreateBeerForm(request.POST)
            if beer_form.is_valid():
                messages.success(request, 'Beer has been created.')
                beer_form.save()
            else:
                ctxt['beer_form'] = beer_form

        return render(
            request, self.template_name, self.get_context_data(**ctxt))


class BeerRatingView(ListView):
    """ Creates a list view of all reviews on website """
    model = BeerReview
    template_name = 'review_list.html'
    paginate_by = 8
    ordering = ['-pub_date']


class BeerStyleCreateView(ListView):
    """ Create a beer style on add review page """
    template_name = 'add_review/create_style.html'
    form_class = CreateBeerStyleForm


class ReviewDetailView(DetailView):
    """ Create a detailed view of every review on website """
    model = BeerReview
    template_name = 'review_list/review_detail.html'


class UpdateReviewView(UpdateView):
    """ Update a review after editing """
    model = BeerReview
    form_class = BeerReviewForm
    template_name = 'review_list/review_update.html'

    def __init__(self):
        self.updform = None

    def form_valid(self, form):
        """  Validate update review form and save it """
        self.updform = form.save(commit=False)
        self.slug = self.updform.beer_style
        self.updform.save()
        return redirect('review_detail', self.updform.pk)


class DeleteReviewView(DeleteView):
    """ Delete a beer review form """
    model = BeerReview
    form_class = BeerReviewForm
    template_name = 'review_list/review_delete.html'
    success_url = reverse_lazy('review_list')


def style_category_view(request, style):
    """ Define beer style view on search """
    style_reviews = BeerReview.objects.filter(slug=style).order_by('-pub_date')
    return render(request, 'review_list/stylecategories.html', {
        'style': style, 'style_reviews': style_reviews})


def cat_style_menu_on_all_pages(_request):
    """ Add beer style view search in all pages """
    return {'cat_style_menu': BeerStyle.objects.all().order_by('beer_style')}


def beer_category_view(request):
    """ Add beer view search in all pages """
    if request.method == "POST":
        searched = request.POST['searched']
    elif request.method == "GET":
        searched = request.GET['searched']

    beers = BeerReview.objects.filter(
        beer__beer_name__icontains=searched).order_by('-pub_date')

    paginator = Paginator(beers, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'review_list/beercategories.html', {
        'searched': searched, 'beer_review': page_obj})
