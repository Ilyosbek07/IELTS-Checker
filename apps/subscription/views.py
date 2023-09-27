from rest_framework import generics

from apps.subscription.models import Subscription, Order
from apps.subscription.serializers import SubscriptionsSerializer, OrderSerializer


class SubscriptionListAPIView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionsSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
