from django.shortcuts import render,redirect
from .models import Room, Topic, User, Message
from .forms import RoomForm, UpdateUser
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    topics=Topic.objects.all()[0:5]
    staff_hosts=User.objects.filter(is_staff=True)
    all_staff_hosts_usernames=[]
    for i in staff_hosts:
        all_staff_hosts_usernames.append(i.username)
    query=request.GET.get('q') if request.GET.get('q')!=None else ''
    if query:
        rooms=Room.objects.filter( 
            Q(host__username__icontains=query) |
            Q(topic__name__icontains=query) |
            Q(name__icontains=query)
            )
    else:
        rooms=Room.objects.all()
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=query))[:5]
    room_count=rooms.count()
    context={'rooms':rooms, 'topics':topics,'room_count':room_count,'all_staff_hosts_usernames':all_staff_hosts_usernames,'room_messages':room_messages}
    return render(request,'base/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        entered_message=request.POST.get('body')
        Message.objects.create(
            user=request.user,
            room=room,
            body=entered_message
        )
        room.participants.add(request.user)
        return redirect('room',pk)
    room_messages=room.message_set.all()
    participants=room.participants.all()
    context={'room':room,'room_messages':room_messages,'participants':participants}
    return render(request,'base/room.html',context)

@login_required
def DeleteMessage(request,pk):
    previous_page=request.META.get('HTTP_REFERER','home')
    print(previous_page)
    room_message=Message.objects.get(id=pk)
    if request.method=='POST':
        room_message.delete()
        return redirect('room', room_message.room_id)
    context={'previous_page':previous_page,'obj':room_message}
    return render(request,'base/delete.html',context)

@login_required
def CreateRoom(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        topic=topic.strip()
        topic,created=Topic.objects.get_or_create(name=topic)
        Room.objects.create(
            host=request.user,
            name=request.POST.get('name'),
            topic=topic,
            description=request.POST.get('description')
        )
        return redirect('home')
    form=RoomForm()
    topics=Topic.objects.all()
    context={'form':form,'topics':topics}
    return render(request,'base/room_form.html',context)


@login_required
def EditRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic_name=topic_name.strip()
        topic,created=Topic.objects.get_or_create(name=topic_name)
        room.topic=topic
        room.name=request.POST.get('name')
        room.description=request.POST.get('description')
        room.save()
        return redirect('home')
    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/update.html', context)

@login_required
def DeleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    
    previous_page=request.META.get('HTTP_REFERER','home')
    context={'room':room,'previous_page':previous_page,'obj':room}
    return render(request,'base/delete.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username doesn't exist")
            return redirect('login')

        user=authenticate(request,username=username,password=password)

        if user!=None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    page='login'
    context={'page':page}
    return render(request,'base/login.html',context) 

def logoutPage(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
    previous_page=request.META.get('HTTP_REFERER','home')
    context={'previous_page':previous_page}
    return render(request,'base/logout.html',context)

def Registerpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password1')
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        newuser=authenticate(request,username=username,password=password)
        login(request,newuser)
        return redirect('home')

    form=UserCreationForm()
    context={'form':form}
    return render(request,'base/login.html',context)

def userProfile(request,pk):
    user=User.objects.get(id=pk)
    topics=Topic.objects.all()
    query=request.GET.get('q') if request.GET.get('q')!=None else ''
    
    if query:
        rooms=Room.objects.filter(
            Q(host=user) &
            (Q(topic__name__icontains=query) |
             Q(name__icontains=query)
            ))
        room_messages=Message.objects.filter(
            Q(user=user) &
            (Q(room__topic__name__icontains=query) |
             Q(room__name__icontains=query)
            ))
    else:
        rooms=Room.objects.filter(host=user)
        room_messages=Message.objects.filter(user=user)
    context={'user':user,'topics':topics,'rooms':rooms,'room_messages':room_messages}
    return render(request,'base/user_profile.html',context)


def updateUser(request):
    user=request.user
    form= UpdateUser(instance=user)
    if request.method=='POST':
        form=UpdateUser(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('user-profile',user.id)
    context={'form':form}
    return render(request,'base/update-user.html',context)

def topicsPage(request):
    query=request.GET.get('q') if request.GET.get('q')!=None else ''
    topics=Topic.objects.filter(name__icontains=query)[0:5]
    context={'topics':topics}
    return render(request,'base/topics.html',context)

def activityPage(request):
    room_messages=Message.objects.all()[0:2]
    context={'room_messages':room_messages}
    return render(request,'base/activity.html',context)