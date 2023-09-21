from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Essay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_essays')
    topic = models.CharField(max_length=255, verbose_name=_('Topic'))
    text = models.TextField()

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = _('Essay')
        verbose_name_plural = _('Essays')
