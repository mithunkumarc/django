from django.shortcuts import render
from django.http import HttpResponse


def setsession(request):
    request.session['sname'] = 'rajat'
    request.session['semail'] = 'rajat.jay@gmail.com'
    return HttpResponse("session is set")


def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    del request.session['sname']  #: use this to delete session
    del request.session['semail']
    return HttpResponse(studentname + " " + studentemail)