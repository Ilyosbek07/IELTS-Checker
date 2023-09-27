from rest_framework import serializers

from apps.subscription.models import Subscription, ExtraInfo, Order


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ('name',)


class SubscriptionsSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=True)

    class Meta:
        model = Subscription
        fields = (
            'plan',
            'coins',
            'price',
            'extra_info'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'subscription',
        )
