""" System Module """
from django.shortcuts import render


def page_not_found_view(request, exception):
    """ 404 error page """
    return render(request, '404.html', status=404)


def my_custom_error_view(request, *args, **argv):
    """ 500 error page """
    return render(request, '500.html', status=500)


def error_403(request, exception):
    """ 403 error page """
    return render(request, '403.html')


def my_custom_bad_request_view(request, exception):
    """ 400 error page """
    return render(request, '400.html')
