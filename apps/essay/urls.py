from django.urls import path

from apps.essay.views import EssayCreateAPIView

urlpatterns = [
    path('create/', EssayCreateAPIView.as_view(), name='essay_create'),
]
