from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.

def about_us(request):
    return HttpResponse("This is the About Us page")
