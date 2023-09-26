from django.contrib import admin

from apps.user.models import Profile, User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ("id", "email")


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ("id", "user")
    ordering = ("-id",)
    list_filter = ("user__status",)
