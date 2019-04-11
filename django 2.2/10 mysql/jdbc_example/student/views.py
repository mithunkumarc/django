from django.shortcuts import render,redirect
from student.form import StuForm
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def index(request):
    stu = StuForm()
    return render(request,"index.html",{'form':stu})


@require_http_methods(["POST"])
def create(request):
    if request.method == "POST":
        form = StuForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print(form.data,' saved')
                return redirect('/student/index')
            except:
                pass
    else:
        form = StuForm()
    return render(request,'index.html',{'form':form})