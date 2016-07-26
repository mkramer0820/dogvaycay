from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # login page
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    #url(r'^register/$', views.register, name='registration_form'),
]

