from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit-profile/', views.edit_profile, name="edit-profile"),
]
