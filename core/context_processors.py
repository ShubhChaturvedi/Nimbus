from .models import *


def message_processor(request):
    key = Key.objects.first()
    user = request.user
    profile = Profile.objects.filter(username=user.username).first()
    following = profile.following.count()
    followers = profile.followers.count()
    return {
        "key": key,
        "user": profile,
        "following": following,
        "followers": followers
    }
