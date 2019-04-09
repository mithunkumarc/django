from django.shortcuts import render
from .forms import StudentForm

def index(request):
    student = StudentForm()
    return render(request,"index.html",{'stu_form':student})
