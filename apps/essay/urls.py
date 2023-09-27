from django.urls import path

from apps.essay.views import EssayCreateAPIView, EssayStatisticsListAPIView, LetterListAPIView, \
    EssayStatisticsRetrieveAPIView, LetterRetrieveAPIView

urlpatterns = [
    path('create/', EssayCreateAPIView.as_view(), name='essay_create'),
    path('statistics/list/', EssayStatisticsListAPIView.as_view(), name='essay_statistics'),
    path('<int:pk>/statistics/', EssayStatisticsRetrieveAPIView.as_view(), name='essay_detail'),
    path('statistics/letter/list/', LetterListAPIView.as_view(), name='letter_statistics'),
    path('<int:pk>/statistics/letter/', LetterRetrieveAPIView.as_view(), name='letter_detail'),
]
