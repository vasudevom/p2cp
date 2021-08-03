from django.contrib import admin

# Register your models here.

from .models import signup_user

admin.site.register(signup_user)