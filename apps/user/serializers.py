from django.core import signing
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.cache import CacheTypes
from apps.user.models import User
from django.utils.translation import gettext_lazy as _


class SendVerificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)


class VerificationRegistrationCodeSerializer(SendVerificationCodeSerializer):
    code = serializers.CharField()
    session = serializers.CharField()


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "token",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "token": {"read_only": True},
        }

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data

    def validate(self, attrs):
        email = attrs.pop("email")
        signer = signing.TimestampSigner()
        email_data = signer.unsign_object(email, max_age=600)
        if email_data.get("type") != CacheTypes.registration_sms_verification:
            raise ValidationError(_("Wrong type!"))
        attrs["email"] = email_data.get("email")
        return attrs

    def create(self, validated_data):
        try:
            user = User.objects.create_user(**validated_data)
        except Exception as e:
            raise ValidationError(str(e))
        return user
