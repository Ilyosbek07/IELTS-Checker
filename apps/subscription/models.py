from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.subscription.choices import PlanChoice
from apps.user.models import User


class ExtraInfo(BaseModel):
    name = models.CharField(_('Name'), max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Extra Info'
        verbose_name_plural = 'Extra Infos'


class Subscription(BaseModel):
    plan = models.CharField(_('Plan'), choices=PlanChoice.choices, max_length=125)
    coins = models.PositiveIntegerField(_('Coins'), default=3)
    price = models.PositiveIntegerField(_('Price'))
    extra_info = models.ManyToManyField(ExtraInfo, related_name='extra_info', verbose_name=_('Extra info'))

    def __str__(self):
        return f'Subscription - {self.plan}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'


class Order(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_order',
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    subscription = models.ForeignKey(
        Subscription,
        related_name='subscription_order',
        on_delete=models.CASCADE,
        verbose_name=_('Subscription')
    )

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f'{self.user} - {self.subscription.plan} order'
