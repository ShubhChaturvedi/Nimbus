from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            print(user)
            print(user.check_password(raw_password= password))
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None