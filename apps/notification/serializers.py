from rest_framework import serializers

from apps.notification.models import Notification, UserNotification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id", "title", "text")


class UserNotificationListSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()

    class Meta:
        model = UserNotification
        fields = (
            "id",
            "user",
            "notification",
            "is_read",
            "created_at",
        )
