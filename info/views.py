from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse


from .forms import DogForm


def blank_form_view(request):
    if request.method == "POST":
        form = DogForm(request.POST)
        if form.is_valid():
            blank_form_view = form.save(commit=False)
            blank_form_view.save()
            return HttpResponseRedirect(reverse('dog_vaycay:index'))
    else:
        form = DogForm()

    context = {'form': form}
    return render(request, 'info/blank_form.html', context)
