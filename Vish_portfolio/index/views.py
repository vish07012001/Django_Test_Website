from django.shortcuts import render
from django.http import HttpResponse
from .models import about,slider,client


# Create your views here.
def home(request):
    text = {
        'names': ['Vishal','Rahul','Rohit','Rajesh','Ravi']
    }
    # Fetching data from database and sending it to the template
    aboutdata = about.objects.all()
    text['aboutdata'] = aboutdata

    # Fetching data from database and sending it to the template
    sliderdata = slider.objects.all()
    text['sliderdata'] = sliderdata

    # Fetching data from database and sending it to the template
    clientdata = client.objects.all()
    text['clientdata'] = clientdata
    
    return render(request,'index.html',text)
    # return HttpResponse("This is Home page")

def about_us(request):
    return render(request,"about.html")

# def contact(request):
#     return render(request,"contact.html")
