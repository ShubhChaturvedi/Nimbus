from .models import *


def message_processor(request):
    key = Key.objects.first()
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    return {
        "key": key,
        "user": profile
    }
