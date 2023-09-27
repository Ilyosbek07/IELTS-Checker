from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.subscription.choices import PlanChoice
from apps.subscription.models import Subscription, ExtraInfo
from apps.user.models import User


# from apps.subscription.models import

class SubscriptionAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='example@gmail.com',
            password='123$321'
        )
        self.extra_info = ExtraInfo.objects.create(
            name='First Info'
        )
        self.subscription = Subscription.objects.create(
            plan=PlanChoice.free,
            coins=3,
            price=150000,
        )
        self.subscription.extra_info.add(self.extra_info)

    def test_subscription_list(self):
        response = self.client.get(reverse("subscription_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)

    def test_order_create(self):
        self.client.force_login(self.user)
        data = {
            'user': self.user.id,
            'subscription': self.subscription.id
        }
        response = self.client.post(reverse("order_create"),data=data)
        self.assertEqual(response.status_code, 201)




