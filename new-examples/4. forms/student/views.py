from django.shortcuts import render

# Create your views here.
from django.shortcuts import render  
from student.form import StuForm  
      
def index(request):  
    stu = StuForm()  
    return render(request,"index.html",{'form':stu})  
