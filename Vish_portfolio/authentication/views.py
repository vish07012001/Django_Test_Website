from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# for messages
from django.contrib import messages
# for registration form
from django.contrib.auth.models import User


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        valid_user_or_not = authenticate(request,username=username,password=password)

        if valid_user_or_not is not None:
            login(request,valid_user_or_not)
            return redirect('profile')
        else:
            messages.error(request,"Invalid username or password")
            # print("Invalid username or password")

    return render(request,'authentication/login.html')

def user_logout(request): 
    logout(request)   
    messages.success(request,"You have been successfully logged out!")
    return redirect('login')


def forgot(request):
    return render(request,'authentication/forgot.html')

def register(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username is already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email is already taken")
            else:
                User.objects.create_user(username=username,email=email,password=password).save()
                messages.success(request,"You have been successfully registered!")
                return redirect('login')

        else:
            messages.error(request,"Password and Confirm Password should be same")
            
    return render(request,'authentication/registration.html')
