__author__ = 'Kramer'

from django.conf.urls import url
from . import views


urlpatterns = [
    # home page
    url(r'^index$', views.index, name='index'),
]