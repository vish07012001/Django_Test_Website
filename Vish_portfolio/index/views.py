from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    text = {
        'names': ['Vishal','Rahul','Rohit','Rajesh','Ravi']
    }
    return render(request,'index.html',text)
    # return HttpResponse("This is Home page")

def about_us(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
