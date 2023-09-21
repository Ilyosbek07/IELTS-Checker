from django.db import models
from django.utils.translation import gettext_lazy as _


class UserStatus(models.TextChoices):
    BASIC = "basic", _("Basic")
    PREMIUM = "premium", _("Premium")
