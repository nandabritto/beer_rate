'''ASGI config for django_beerapp project.'''

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_beerapp.settings')

application = get_asgi_application()
