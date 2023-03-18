from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    return redirect("/accounts/login")