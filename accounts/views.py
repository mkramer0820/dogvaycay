from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreateForm, UserProfileForm


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


def profile(request):
    if request.method != 'POST':
        # display blank registration form
        form = UserProfileForm()
    else:
        # process complete form
        form = UserProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('dog_vaycay:index'))

    context = {'form': form}
    return render(request, 'accounts/user_profile.html', context)


"""
def profile(request):
    if request.method == "POST":
        form = UserProfile(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dog_vaycay:index'))
    else:
        form = UserProfile()

    context = {'form': form}
    return render(request, 'accounts/user_profile.html', context)
"""