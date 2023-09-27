import random
import string

from django.core import signing
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.cache import CacheTypes, generate_cache_key
from apps.user.serializers import SendVerificationCodeSerializer, VerificationRegistrationCodeSerializer, \
    RegisterUserSerializer
from apps.user.models import User
from apps.user.shared import send_verification_code
from django.core.cache import cache


class SendVerificationCodeAPIView(APIView):
    @swagger_auto_schema(request_body=SendVerificationCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = SendVerificationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        self.check_user_exists(email)
        session = "".join(random.choice(string.ascii_lowercase) for _ in range(12))
        send_verification_code(email, CacheTypes.registration_sms_verification, session)
        return Response({"session": session})

    @staticmethod
    def check_user_exists(email):
        if User.objects.filter(email=email):
            raise ValidationError(f"User exist with this email: {email}")


class VerificationRegistrationCodeAPIView(APIView):
    @swagger_auto_schema(request_body=VerificationRegistrationCodeSerializer)
    def post(self, request, *args, **kwargs):
        # Deserialize the request data using your serializer
        serializer = VerificationRegistrationCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract validated data from the serializer
        email = serializer.validated_data.get("email")
        code = serializer.validated_data.get("code")
        session = serializer.validated_data.get("session")

        # Generate a cache key for the code validation
        cache_key = generate_cache_key(CacheTypes.registration_sms_verification, email, session)

        # Check if the code is valid
        if not self.is_code_valid(cache_key, code):
            return Response({"detail": "Wrong code!"}, status=status.HTTP_400_BAD_REQUEST)

        # Sign and prepare the response data
        signer = signing.TimestampSigner()
        email_data = signer.sign_object({"email": email, "type": CacheTypes.registration_sms_verification})

        # Return the response
        return Response({"email": email_data})

    def check_user_exists(self, email):
        # Check if a user with the given email exists
        if User.objects.filter(email=email).exists():  # Use .exists() for efficiency
            raise ValidationError(f"User exists with this email: {email}")

    def is_code_valid(self, cache_key, code):
        # Check if the provided code matches the cached code
        valid_code = cache.get(cache_key)
        return valid_code == code


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
