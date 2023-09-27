from django.contrib import admin

from apps.notification.models import Notification, UserNotification

admin.site.register(Notification)
admin.site.register(UserNotification)
