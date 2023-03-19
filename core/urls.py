from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('edit-profile/', views.edit_profile, name="edit-profile"),
    path('my-account/', views.my_account, name="my-account"),
    path('handleUploadProfile', views.handleUploadProfile, name="uploadprofile"),
    path('connections', views.connections, name="connections"),
]
