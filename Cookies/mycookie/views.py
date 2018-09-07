from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('name', 'rajat')
    #response.delete_cookie('name') : run this line to delete value of cookie 'name'
    return response


def getcookie(request):
    name = request.COOKIES['name']
    return HttpResponse("name @: " + name);