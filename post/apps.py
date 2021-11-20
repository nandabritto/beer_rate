""" System Module """
from django.apps import AppConfig


class PostConfig(AppConfig):
    """ Add post app configurations """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
