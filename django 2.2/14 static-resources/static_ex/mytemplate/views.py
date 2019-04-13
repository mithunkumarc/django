from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('index.html')
    name = {
        'message': 'this is a template example'
    }
    return HttpResponse(template.render(name))	