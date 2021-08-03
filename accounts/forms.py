#p2c-21-105

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class EditUser(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        labels={'email':'Email'}

