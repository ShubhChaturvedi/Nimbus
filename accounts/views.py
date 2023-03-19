from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.mail import send_mail


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # messages.success(request,"Your id has been successfully registered")
            # messages.success(request, "Successfully Logged In")
            if(request.user.is_authenicated):
                send_mail(
                'Testing',
                'Test mail.',
                'yashagarwal9389@gmail.com',
                ['yashagarwal9389@gmail.com'],
                fail_silently=False,
                )
            return redirect('/dashboard/')
    return render(request, "accounts/sign-in.html")


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("user")
        email = request.POST.get("email")
        password = request.POST.get("password")

        myuser = Profile(username=username, email=email, first_name=first_name, last_name=last_name)
        myuser.set_password(password)
        myuser.save()

        auth_login(request, myuser)

        return redirect('/dashboard/')

    return render(request, "accounts/sign-up.html")


def logout(request):
    auth_logout(request)
    return redirect("/accounts/login")


def forgotPwd(request):
    return render(request, "accounts/forgot-password.html")
