from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Website_Name', 'Meta_Desc', 'Favicon', 'Logo', 'Email', 'Facebook', 'Instagram', 'Twitter')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'Image', 'Date')
