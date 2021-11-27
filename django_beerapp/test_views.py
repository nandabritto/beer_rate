from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path


def test_page_not_found_view(request, exception=None):
    assertEqual(response.status_code, 403)
