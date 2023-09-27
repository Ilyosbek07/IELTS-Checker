from django.urls import path

from apps.subscription.views import SubscriptionListAPIView, OrderCreateAPIView

urlpatterns = [
    path('order/create/', OrderCreateAPIView.as_view(), name='order_create'),
    path('list/', SubscriptionListAPIView.as_view(), name='subscription_list')
]
