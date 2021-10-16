from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})

def add_review(request):
    return render(request, 'add_review.html', {})