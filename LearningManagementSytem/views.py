from django.shortcuts import render, redirect
from .models import UserProfile, ContactUs
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.core.mail import send_mail

# import random

def home(request):
    return render(request, "index.html")

def login_call(request):
    h = request.POST.get('username')
    i = request.POST.get('pwd')

    user = authenticate(username=h, password=i)

    if user:
        login(request, user)
        uObj = UserProfile.objects.get(user__username=request.user)

        if uObj.role == "Student":
            return redirect('/student/dashboard/')
        elif uObj.role == "Teacher":
            return redirect('/instructor/dashboard/')
        else:
            return redirect('/home/')
    else:
        return redirect('/home/')

def logout_call(request):
    logout(request)
    return redirect('/home/')

def signup(request):
    a = request.POST.get('fname')
    b = request.POST.get('lname')
    c = request.POST.get('urole')
    d = request.POST.get('uemail')
    e = request.POST.get('umobile')
    f = request.POST.get('upassword')
    g = request.POST.get('usrname')

    u = User(username=g, password=make_password(f), first_name=a, last_name=b, email=d)
    u.save()

    up = UserProfile(user=u, mobile=e, role=c)
    up.save()

    return redirect('/home/')

def contactus(request):
    a = request.POST.get('name')
    b = request.POST.get('email')
    c = request.POST.get('mobile')
    d = request.POST.get('message')

    con = ContactUs(name=a, email=b, phone=c, message=d)
    con.save()

    return redirect('/home/')