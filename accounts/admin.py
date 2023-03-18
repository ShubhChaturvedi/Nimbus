from django.contrib import admin
from .models import *


# Register your models here.

class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class DOBInline(admin.StackedInline):
    model = DOB
    extra = 1


class SocialInline(admin.StackedInline):
    model = Social
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [SkillInline, DOBInline, SocialInline]
    exclude = ('password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions')
    list_display = ('username', 'email', 'phone', 'website', 'location', 'bio', 'profile_image', 'job_experience', 'is_email_verified')
