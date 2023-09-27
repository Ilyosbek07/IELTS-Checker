from django.db import models
from django.utils.translation import gettext_lazy as _

class PlanChoice(models.TextChoices):
    free = 'FREE', _('FREE')
    premium_15 = 'PREMIUM 15', _('PREMIUM 15')
    premium_25 = 'PREMIUM 25', _('PREMIUM 25')
