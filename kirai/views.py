from django.shortcuts import render
from .models import Destination

# Create your views here.


def  index(request):
    
    
    dest1=Destination()
    dest1.name="lapii"
    dest1.desc="brand new"
    dest1.price=80099
    dest1.id=1
    
    dest2=Destination()
    dest2.name="matress"
    dest1.desc="heavy duty"
    dest2.price=78759
    dest2.id=2
    
    dest3=Destination()
    dest3.name="Wheelchair"
    dest3.desc="401 Japan Style"
    dest3.price=4000
    dest3.id=3
    
    dest4=Destination()
    dest4.name="Samsung Galaxy"
    dest4.desc="4gb RAM 32gb ROM"
    dest4.price=13000
    dest4.id=4
    
    dest5=Destination()
    dest5.name="My Girl Cheroo"
    dest5.desc="Best Thing That have Happen in my life"
    dest5.price=10000000000000000000000000000000000000
    dest5.id=5
    
    dest6=Destination()
    dest6.name="Crying Pendo"
    dest6.desc="Sumbua"
    dest6.price=5000
    dest6.id=6
    
    
    dest7=Destination()
    dest7.name="Mathees Tv"
    dest7.desc="42 Inches"
    dest7.price=25000
    dest7.id=7
    
    
    dests=[dest1,dest2,dest3,dest4,dest5,dest6,dest7]
    
    context={"dests":dests}
    
    return render(request,'homepage1.html',context)

def home(request):
    return render(request,'kirai/kirai.html')