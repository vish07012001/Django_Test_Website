from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    text = {
        'names': ['Vishal','Rahul','Rohit','Rajesh','Ravi']
    }
    return render(request,'index.html',text)
    # return HttpResponse("This is Home page")