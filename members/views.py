""" System Module """
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def login_user(request):
    """ Login User with username and password, return a message to inform
    if logged or not """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in. :)"))
            return redirect('home')
        else:
            messages.error(request, (
                'There was an error logging in. Username or Password are not \
                    correct. Please, Try again.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    """ Logut user and redirect to Home page """
    logout(request)
    messages.success(request, ('You were logged out. See you soon! :)'))
    return redirect('home')


def register_user(request):
    """ Register User and inform the status by message """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/register_user.html', {
        'form': form,
         })
