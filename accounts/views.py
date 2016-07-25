from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


def logout_view(request):
    """log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('dog_vaycay:index'))