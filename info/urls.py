
from django.conf.urls import url

from . import views


urlpatterns = [
    # info form page
    url(r'^blank_form/$', views.blank_form_view, name='blank_form')
]
