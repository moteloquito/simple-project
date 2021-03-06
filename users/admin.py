from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import CustomUser


class CustomUserInline(admin.StackedInline):

    model = CustomUser


class CustomUserAdmin(UserAdmin):

    inlines = [CustomUserInline, ]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
