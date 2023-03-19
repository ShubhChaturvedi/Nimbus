from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit-profile', views.edit_profile, name="edit-profile"),
    path('profile/<str:username>', views.profile, name="my-account"),
    path("api/like", views.handlelikes, name="like"),
]
