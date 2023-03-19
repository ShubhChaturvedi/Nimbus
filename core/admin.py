from django.contrib import admin
from .models import *


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class LikeInline(admin.StackedInline):
    model = Like
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, LikeInline]
    list_display = ('user', 'description', 'Image', 'Date', 'comment_count')


# Register your models here.
@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Website_Name', 'Meta_Desc', 'Favicon', 'Logo', 'Email', 'Facebook', 'Instagram', 'Twitter')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following', 'Date')
