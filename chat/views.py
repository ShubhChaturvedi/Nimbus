from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def chatIndex(request):
    return HttpResponse("Welcome to chat")

def roomName(request, room_name):
    return HttpResponse("Welcome to chat room")