from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from .backends import EmailBackend


# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            # messages.success(request,"Your id has been successfully registered")
            # messages.success(request, "Successfully Logged In")
            return redirect('/dashboard/')
    return render(request, "accounts/sign-in.html")
    
def signup(request):
    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = first_name + " " + last_name
        email = request.POST.get("email")
        password = request.POST.get("password")

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            # messages.success(request,"Your id has been successfully registered")
            # messages.success(request, "Successfully Logged In")
            return redirect('/dashboard/')

    return render(request, "accounts/sign-up.html")

def logout(request):
    auth_logout(request)
    return redirect("/accounts/login")

def forgotPwd(request):
    return render(request, "accounts/forgot-password.html")