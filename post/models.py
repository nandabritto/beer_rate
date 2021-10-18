from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
import numpy as np


class BeerStyle(models.Model):
    beer_style = models.CharField(max_length=200, unique=True)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __str__(self):
        return self.beer_style

class Beer(models.Model):
    beer_name = models.CharField(max_length=200)
    style = models.ManyToManyField(BeerStyle)
    
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)
        
    def __str__(self):
        return self.beer_name


class BeerReview(models.Model):
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

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    beer_style = models.CharField(max_length=200)
    beer = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    bitterness = models.IntegerField(choices=BITTERNESS_CHOICES)
    money_value = models.IntegerField(choices=MONEY_VALUE_CHOICES)
    # rating = models.IntegerField(choices=RATING_CHOICES)#
    
    def __str__(self):
        return self.beer + '|' + str(self.user_name)

    def get_absolute_url(self):
        return reverse('beer-rate', kwargs={'pk': self.pk})
    



