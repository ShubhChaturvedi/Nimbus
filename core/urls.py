from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit-profile', views.edit_profile, name="edit-profile"),
    path('profile/<str:username>', views.profile, name="my-account"),
    path("api/like", views.handlelikes, name="like"),
    path("api/comment", views.handelcomment, name="comment"),
    path("api/follow", views.handlefollow, name="follow"),
]
