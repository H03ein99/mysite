from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_views(requests):
    return HttpResponse('<h1> here is home page </h1>')

def about_views(requests):
    return HttpResponse('this is about me')

def contact_views(requests):
    return HttpResponse('contact me here')