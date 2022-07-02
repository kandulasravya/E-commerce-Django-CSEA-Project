from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from core.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_login(request):
    if request.method=="POST": 
        username=request.POST.get('username')   
        password=request.POST.get('password') 
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        messages.info(request,"Login Failed, Please Try Again")
            

    return render(request,'accounts/login.html')   
    

def user_register(request):
    if request.method=="POST":
           username=request.POST.get('username')
           email=request.POST.get('email') 
           password=request.POST.get('password') 
           confirm_password=request.POST.get('confirm_password') 
           phone=request.POST.get('phone_field')
          # print(username,email) 
           if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already Exists!")
             #print("Invalid username")
                return redirect(user_register)
            else:
                 if User.objects.filter(email=email).exists():
                   # print("email already exists ")
                    messages.info(request,"Email already Exists!")
                    return redirect('user_register')
                 else:
                    user=User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    data=Customer(user=user,phone_field=phone)
                    data.save()
                    #code for login will come here
                    our_user = authenticate(username=username,password=password)
                    if our_user is not None:
                        login(request,user)
                        return redirect('/')
                    else:
                       # print("Error here...")  
                          messages.info(request,"Password and Confirm Password Mismatch!")
                          return redirect('user_register') 
           # user=user.objects.create_user(username=username,password=password,email=email)

    return render(request,'accounts/register.html')

def user_logout(request):
    logout(request)
    return redirect('/')