from django import forms

from .models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['dogs_name', ]
        labels = {'dogs_name': ''}
