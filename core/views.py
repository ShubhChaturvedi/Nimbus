from django.conf import settings
from django.shortcuts import render, redirect
# import login_required
from django.contrib.auth.decorators import login_required
from accounts.models import *
from django.core.files.storage import FileSystemStorage


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
            from_date = request.POST.get("from_date")
            to_date = request.POST.get("to_date")
            company = request.POST.get("company")
            designation = request.POST.get("designation")
            description = request.POST.get("description")
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
                dob = DOB.objects.create(month=month, day=day, year=year, user=profile, gender=gender)


            exp = Experience(from_date=from_date, to_date=to_date, company=company,
                             designation=designation, description=description, user=profile)

            exp.save()
            dob.save()
            profile.save()
        if request.POST.get("btn") == "socials":
            user = request.user
            profile = Profile.objects.filter(username=user.username).first()
            instagram = request.POST.get("instagram")
            facebook = request.POST.get("facebook")
            twitter = request.POST.get("twitter")
            youtube = request.POST.get("youtube")
            github = request.POST.get("github")
            if profile.social_set.first() is not None:
                social = profile.social_set.first()
                social.instagram = instagram
                social.facebook = facebook
                social.twitter = twitter
                social.youtube = youtube
                social.github = github
            else:
                social = Social.objects.create(instagram=instagram, facebook=facebook, twitter=twitter,
                                               youtube=youtube, github=github, user=profile)


    user = request.user

    profile = Profile.objects.filter(username=user.username).first()

    social = profile.social_set.first()
    return render(request, 'dashboard/edit-profile.html', context={
        'profile': profile,
        'social': social
    })


@login_required
def my_account(request):
    all_users = Profile.objects.order_by("?")[:5]
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    return render(request, "dashboard/profile.html", context={'profile': profile,'all_users':all_users})


def handleUploadProfile(request):
    if request.method == "POST" and request.FILES['profile']:
        profField = Profile.objects.filter(username=request.user.username).first()
        # get upload to location from profile model
        upload = request.FILES['profile']
        fss = FileSystemStorage()
        fss.location = settings.MEDIA_ROOT / "user/profile"
        file = fss.save(upload.name, upload)
        profField.profile_image = "user/profile/" + str(file)
        profField.save()
        return redirect('/dashboard/edit-profile')

def connections(request):
    all_users = Profile.objects.order_by("?")[:9]
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    return render(request, "dashboard/connection.html", context={'profile': profile, 'all_users': all_users})

