# custom_backends.py

from django.contrib.auth.backends import ModelBackend
from .models import DoctorUser

class DoctorUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = DoctorUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except DoctorUser.DoesNotExist:
            return None
