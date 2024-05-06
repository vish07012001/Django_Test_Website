from django.shortcuts import render
from .models import contactlist,contactform

# Create your views here.
def contact(request):
    # For HTML form submission
    if request.method == "POST":
        name =  request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message =  request.POST.get("message")  

        # Saving data to the database
        contactform(name=name,email=email,subject=subject,messgae=message).save()

    # Fetching data from database and sending it to the template    
    text={}
    contactdata = contactlist.objects.all()
    text['contactdata'] = contactdata
    return render(request,"contact.html",text)