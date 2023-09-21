from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.user.choices import UserStatus


class UserManager(AbstractUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    status = models.CharField(
        max_length=9, choices=UserStatus.choices, verbose_name=_("User status"), default=UserStatus.BASIC
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # type: ignore

    objects = UserManager()

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=128, verbose_name=_("Full name"))
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="profile/pictures", null=True, blank=True)
    birth_date = models.DateField(verbose_name=_("Birth date"), null=True, blank=True)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profile")

    def __str__(self):
        return self.full_name
