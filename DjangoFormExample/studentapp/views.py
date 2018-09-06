from django.shortcuts import render
from studentapp.form import StudentForm


def index(request):
    stu = StudentForm()
    return render(request, "index.html", {'form': stu})