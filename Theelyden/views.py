from django.shortcuts import render 
#from .models import  Room
# Create your views here.
#import datetime

#year=datetime.datetime.now().strftime("%Y")
#context={"year":year}
#def home(request):
 #   return render(request,'Theelyden/homepage.html',context)

#def createaccount(request):
 #   return render (request,'Theelyden/createaccount.html',context)



#def login(request):
 #   return render(request,'Theelyden/loginpage.html',context)

#def verify(request):
 #   username=request.POST['username']
  #  password=request.POST['password']
   # context={"results":{'username':username,'password':password}}
    #return render(request,'Theelyden/results.html',context)
    
    
    
def home(request):
    return render(request,"Theelyden/theelyden.html")