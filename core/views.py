from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
# import login_required
from django.contrib.auth.decorators import login_required
from accounts.models import *
from .models import *
from django.db.models import Q

# Create your views here.


def index(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            description = request.POST.get("description")
            image = request.FILES.get('images')
            profile = Profile.objects.get(username=request.user.username)
            post = Post(description=description, user=profile)

            if image is not None:
                fss = FileSystemStorage()
                fss.location = settings.MEDIA_ROOT / "user/profile"
                file = fss.save(image.name, image)
                post.Image = "user/profile/" + file
            post.save()
            return redirect('/dashboard/')

        all_users = Profile.objects.filter(~Q(username=request.user.username)).order_by("?")[:5]
        return render(request, 'dashboard/index.html', context={'all_users': all_users})
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
                dob = DOB.objects.create(month=month, day=day, year=year, user=profile, gender=gender)

            dob.save()
            profile.save()

    user = request.user
    profile = Profile.objects.filter(username=user.username).first()

    social = profile.social_set.first()
    return render(request, 'dashboard/edit-profile.html', context={
        'profile': profile,
        'social': social
    })


@login_required
def profile(request, username):
    user = Profile.objects.filter(username=username).first()
    if not user:
        return redirect('/dashboard')
    profile = Profile.objects.filter(username=user.username).first()
    return render(request, "dashboard/profile.html", context={'profile': profile})


def handleUploadProfile(request):
    if request.method == "POST" and request.FILES['image']:
        profField = Profile.objects.filter(username=request.user.username).first()
        # get upload to location from profile model
        upload = request.FILES['profile']
        fss = FileSystemStorage()
        fss.location = settings.MEDIA_ROOT / "user/profile"
        file = fss.save(upload.name, upload)
        profField.profile = file
        profField.save()
        return redirect('/dashboard/edit-profile')


def handlelikes(request):
    print(request.user)
    if request.method == "POST":
        post_id = request.POST.get("post_id")
    return redirect('/dashboard')
def handelcomment(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        comment = request.POST.get("comment")
        post = Post.objects.get(id=post_id)
        profile = Profile.objects.get(username=request.user.username)
        comment = Comment.objects.create(user=profile, post=post, comment=comment)
        comment.save()
        return redirect('/dashboard')