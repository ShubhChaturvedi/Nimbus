from django.db import models


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

