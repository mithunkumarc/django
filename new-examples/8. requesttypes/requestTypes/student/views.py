from django.shortcuts import render,redirect  
from student.forms import StuForm  
from django.http import HttpResponse  
from django.views.decorators.http import require_http_methods  

def index(request):  
    stu = StuForm()  
    return render(request,"index.html",{'form':stu})


# @require_http_methods(["POST"]) only accepts post 
def create(request):
    if request.method == "POST":  
            form = StuForm(request.POST)  
            if form.is_valid():  
                try:  
                    print('post data')
                    print(form.data)  
                    return redirect('/student/index')
                except:  
                    pass      
    if request.method == "GET":  
            form = StuForm(request.GET)  
            if form.is_valid():  
                try:  
                    print('get data')
                    print(form.data)  
                    return redirect('/student/index')
                except:  
                    pass  
    else:  
        form = StuForm()  
        return render(request,'index.html',{'form':form})
    



def special_case_2003(request):
    return HttpResponse('special_case_2003')
    
    
def year_archive(request,year):
    return HttpResponse('year_archive')
    

def month_archive(request,year,month):
    return HttpResponse('month_archive')
    

def message_page(request):
    message =  request.GET.get('message')
    return HttpResponse(message)