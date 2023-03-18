from django.shortcuts import render, redirect
# import login_required
from django.contrib.auth.decorators import login_required
from accounts.models import *

# Create your views here.


def index(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    return redirect('/accounts/login')


@login_required
def edit_profile(request):

    if request.method == 'POST':
        if request.POST.get("btn") == "profile":
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("email")
            username = request.POST.get("user")
            website = request.POST.get("website")
            location = request.POST.get("location")
            phone = request.POST.get("phone")

            month = request.POST.get("month")
            day = request.POST.get("day")
            year = request.POST.get("year")
            gender = request.POST.get("gender")

            print(fname, lname, email, username, website, location, phone)

            user = request.user
            profile = Profile.objects.filter(username=user.username).first()
            profile.first_name = fname
            profile.last_name = lname
            profile.email = email
            if not Profile.objects.filter(username=username).exists():
                profile.username = username
            profile.website = website
            profile.location = location
            profile.phone = phone

            if profile.dob_set.first() is not None:
                dob = profile.dob_set.first()
                dob.month = month
                dob.day = day
                dob.year = year
            else:
                dob = DOB.objects.create(month=month, day=day, year=year, profile=profile, gender=gender)

            dob.save()
            profile.save()

    user = request.user
    profile = Profile.objects.filter(username=user.username).first()

    social = profile.social_set.first()
    return render(request, 'dashboard/edit-profile.html', context={
        'profile': profile,
        'social': social
    })
    return render(request, 'dashboard/edit-profile.html', context={'profile': profile})


@login_required
def my_account(request):
    all_users = Profile.objects.order_by("?")[:5]
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    return render(request, "dashboard/profile.html", context={'profile': profile,'all_users':all_users})
