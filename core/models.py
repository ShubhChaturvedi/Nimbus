import uuid

from django.db import models
from accounts.models import Profile


# Create your models here.
class Key(models.Model):
    Name = models.CharField(max_length=1000)
    Website_Name = models.CharField(max_length=1000, null=True, blank=True)
    Meta_Desc = models.CharField(max_length=1000, null=True, blank=True)
    # Copyright = models.CharField(max_length=1000, null=True)
    Favicon = models.ImageField(upload_to="Logo", null=True, blank=True)
    Logo = models.ImageField(upload_to="Logo", null=True, blank=True)
    # Add = models.TextField(max_length=1000)
    Email = models.EmailField(max_length=1000, null=True, blank=True)
    # Phone = models.CharField(max_length=1000, null=True)
    Facebook = models.CharField(max_length=1000, null=True, blank=True)
    Instagram = models.CharField(max_length=1000, null=True, blank=True)
    Twitter = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.Name


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # heading = models.CharField(max_length=1000)
    description = models.TextField(max_length=100000)
    Image = models.ImageField(upload_to="Post", null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " liked " + self.post.Title


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100000)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " commented on " + self.post.Title


class Follow(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="following")
    Date = models.DateTimeField(auto_now_add=True)
    # UUID Field
    roomcode = models.UUIDField(default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.user.username + " following " + self.following.username


