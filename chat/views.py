from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def chatIndex(request):
    return render(request, 'dashboard/messages.html', {"room_name": ""})


def roomName(request, room_name):
    return render(request, 'dashboard/messages.html', {
        "room_name": room_name
    })
