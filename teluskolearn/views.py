
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.

dests=Product.objects.all()

context={"dests":dests}

def  index(request):
    
    return render(request,'teluskolearn/homepage.html',context)

def home(request):
    return render(request,"teluskolearn/telusko.html")


def createaccount(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            email=request.POST['email'].lower()
            password1=request.POST['password1']
            password2=request.POST['password2']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            
            if password1 == password2:
                if User.objects.filter(email=email):
                    messages.error(request,'Email address has been taken')
                    return redirect('createaccount')
                else:
                    user=User.objects.create_user(username="xxxxxx",first_name=firstname,last_name=lastname ,email=email,password=password1)
                    user.save()
                    messages.info(request,'Account created successfully')
                    return render(request,'teluskolearn/homepage.html',context) 
            else:
                messages.error(request,"Passwords doesn't match")
                return redirect('createaccount')
        else:
            return render(request,'teluskolearn/createaccount.html')
    

def login_func(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            email=request.POST['email'].lower()
            password=request.POST['password']
            
            
            #looking app user using email
            try:
                user=User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request,"User does not exists")
                return redirect('login')
                
            
            #validating password
            user=authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'Login Succesful')
                return redirect('teluskohomepage')
            else:
                messages.error(request,"You have enterred wrong user details,check and try again")
                return redirect('login')
        else:
            return render(request,'teluskolearn/loginpage.html')
    
    
def logout_func(request):
    logout(request)
    return redirect('teluskohomepage')