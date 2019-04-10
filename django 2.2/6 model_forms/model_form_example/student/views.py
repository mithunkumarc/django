from django.shortcuts import render
from .form import StuForm

def index(request):
    stu = StuForm()
    return render(request,"index.html",{'stu_form':stu})