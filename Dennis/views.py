from django.shortcuts import render,redirect
from .models import *
from .roomforms import RoomForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def home(request):
    topics=Topic.objects.all()
    q=request.GET.get('q') if request.GET.get('q') !=None else ''
    
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q)|Q(name__icontains=q)|Q(desc__icontains=q)
    )
    all_messages=Message.objects.filter(Q(room__name__icontains=q))
    rooms_count=rooms.count()
    context={'rooms':rooms,'topics':topics,'rooms_count':rooms_count,"all_messages":all_messages}
    return render(request,'Dennis/home.html',context)


def room(request,pk):
    try:
        request=request
        room=Room.objects.get(id=pk)
        messages=room.message_set.all().order_by('-date_modified')
        participants=room.participants.all()
        if request.method=="POST":
            message=Message.objects.create(
                user=request.user,
                room=room,
                body=request.POST.get('comment'),
            )
            room.participants.add(request.user)
            return redirect('room',pk=room.id)
        message_count=messages.count()
        context={'room':room,"messages":messages,"message_count":message_count,"participants":participants,"request":request }
        return render(request,'Dennis/room.html',context)
    except Exception:
        return redirect('home')
    

@login_required(login_url='login')
def createroom(request):
     form=RoomForm() 
     if request.method=='POST':
         form = RoomForm(request.POST)
         if form.is_valid():
             form.save()
             print('room added')
             return redirect('home')
         
         else:
             return redirect('createroom')
     else:
         form.host=request.user.username
         context={"form":form}
         return render(request,"Dennis/room_form.html",context) 
    
    
@login_required(login_url='login') 
def updateroom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    if request.method=="POST":
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context={"form":form}
            return redirect('Dennis/room_form.html',context)
    context={"form":form}
    return render(request,'Dennis/room_form.html',context)
@login_required(login_url='login') 
def deleteroom(request,pk):
    room=Room.objects.get(id=pk)
    if request.user!= room.host:
        messages.error(request,'You are not allowed to to delete this room')
        return redirect('home')
    else: 
        if request.method=='POST':
            room.delete()
            return redirect('home')
        else:
            return render(request,'Dennis/delete.html',{'obj':room})
        
def comment(request):
    if request.POST.get("comment").length !="":
        user=request.user
        comment_content=request.POST['comment']
        
@login_required(login_url='login') 
def deletemessage(request,pk):
    message=Message.objects.get(id=pk)
    if request.user!= message.user:
        messages.error(request,'You are not allowed to to delete this message')
        return redirect('home')
    else: 
        if request.method=='POST':
            message.delete()
            return redirect('home')
        else:
            return render(request,'Dennis/delete.html',{'obj':message})