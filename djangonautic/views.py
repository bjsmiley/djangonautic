from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'djn/homepage.html')

def about(request):
    return render(request, 'djn/about.html')