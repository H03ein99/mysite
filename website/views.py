from django.shortcuts import render

# Create your views here.

def index_views(requests):
    return render(requests, 'website/index.html')

def about_views(requests):
    return render(requests, 'website/about.html')

def contact_views(requests):
    return render(requests, 'website/contact.html')