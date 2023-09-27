from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.user.views import SendVerificationCodeAPIView, VerificationRegistrationCodeAPIView, RegisterAPIView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login",),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("send-code/", SendVerificationCodeAPIView.as_view(),name="send_code"),
    path("verify/code/", VerificationRegistrationCodeAPIView.as_view(), name="verification_code"),
    path("register/", RegisterAPIView.as_view(), name="register"),
]
