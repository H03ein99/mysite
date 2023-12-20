from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_views(requests):
    return render(requests, 'website/index.html')

def about_views(requests):
    return render(requests, 'website/about.html')

def contact_views(requests):
    return render(requests, 'website/contact.html')