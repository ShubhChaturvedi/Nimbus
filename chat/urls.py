from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chatIndex, name="chatIndex"),
    path('<str:room_name>/', views.roomName, name="roomName")
]