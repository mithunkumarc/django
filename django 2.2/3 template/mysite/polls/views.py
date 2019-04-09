from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')  # getting our template
    name = {
        'message': 'this is a template example'
    }
    return HttpResponse(template.render(name))  # rendering the template in HttpResponse