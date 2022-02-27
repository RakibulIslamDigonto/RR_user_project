from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


# Register your models here.
user=get_user_model()

admin.site.unregister(Group)
admin.site.register(user)
