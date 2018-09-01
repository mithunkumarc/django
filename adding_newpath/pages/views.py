from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')

def subPageView(request):
    return HttpResponse('<h1>hello sub page</h1>')