from django.shortcuts import render
# Create your views here.


def index(request):
    """the home page for dog vaycay"""
    return render(request, 'dog_vaycay/index.html')


