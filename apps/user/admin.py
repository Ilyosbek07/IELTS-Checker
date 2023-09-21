from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "email")
