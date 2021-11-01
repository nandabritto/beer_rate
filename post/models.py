from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class BeerStyle(models.Model):
    '''Create a beer style model form'''

    beer_style = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.beer_style

    def get_absolute_url(self):
        return reverse('add_review')


class Beer(models.Model):
    '''Create a beer model form'''
    beer_name = models.CharField(max_length=200, unique=True)
    style = models.ManyToManyField(BeerStyle)

    def __str__(self):
        return self.beer_name

    def get_absolute_url(self):
        return reverse('home')


class BeerReview(models.Model):
    '''Create a beer review model form'''

    BITTERNESS_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    MONEY_VALUE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    beer_style = models.ForeignKey(
        BeerStyle, on_delete=models.CASCADE)
    beer = models.ForeignKey(
        Beer, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE)
    review = models.TextField(max_length=200)
    bitterness = models.IntegerField(choices=BITTERNESS_CHOICES, default=0)
    money_value = models.IntegerField(choices=MONEY_VALUE_CHOICES, default=0)
    beer_image = CloudinaryField('image', blank=True)
    score = models.IntegerField()

    def __str__(self):
        return str(self.beer)

    def get_absolute_url(self):
        return reverse('review_list', kwargs={'pk': self.pk})


beer_review = BeerReview.objects.all()
