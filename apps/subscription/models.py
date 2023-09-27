from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.user.models import User


class ExtraInfo(BaseModel):
    name = models.CharField(_('Name'), max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Extra Info'
        verbose_name_plural = 'Extra Infos'


class SubScription(BaseModel):
    class PlanChoice(models.TextChoices):
        free = 'FREE', _('FREE')
        premium_15 = 'PREMIUM 15', _('PREMIUM 15')
        premium_25 = 'PREMIUM 25', _('PREMIUM 25')

    user = models.ForeignKey(
        User,
        related_name='user_subscription',
        on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    plan = models.CharField(_('Plan'), choices=PlanChoice.choices, max_length=125)
    coins = models.PositiveIntegerField(_('Coins'), default=3)
    price = models.PositiveIntegerField(_('Price'))
    extra_info = models.ManyToManyField(ExtraInfo, related_name='subcription')

    def __str__(self):
        return f'{self.user} - {self.plan}'

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
