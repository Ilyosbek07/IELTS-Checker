from django.contrib import admin

from apps.subscription.models import Subscription, ExtraInfo, Order

admin.site.register(Subscription)
admin.site.register(ExtraInfo)
admin.site.register(Order)
