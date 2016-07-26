from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm


def logout_view(request):
    """log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('dog_vaycay:index'))


def register(request):
    if request.method != 'POST':
        # display blank registration form
        form = UserCreateForm
    else:
        # process complete form
        form = UserCreateForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('dog_vaycay:index'))

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


"""
def register(request):
    if request.method != 'POST':
        # display blank registration form
        form = UserCreationForm
    else:
        # process complete form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('dog_vaycay:index'))

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
"""
