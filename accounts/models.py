from django.db import models
from django.contrib.auth.models import User
from base.models import *


# Create your models here.

class Profile(User):
    class Meta:
        verbose_name_plural = "Profiles"

    is_email_verified = models.BooleanField(default=False)
    phone = models.CharField(max_length=100, null=True, blank=True)
    website = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=1000, null=True, blank=True)
    about = models.TextField(max_length=10000, null=True, blank=True)
    profile_image = models.ImageField(upload_to="user/profile", null=True, blank=True)
    job_experience = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username


class Skill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=100, null=True, blank=True)


class Social(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    youtube = models.CharField(max_length=100, null=True, blank=True)


class DOB(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    day = models.CharField(max_length=100, null=True, blank=True)
    month = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)


