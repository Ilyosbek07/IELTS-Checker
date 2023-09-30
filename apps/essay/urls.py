from django.urls import path

from apps.essay.views import EssayCreateAPIView, LetterContentRetrieveAPIView, EssayContentRetrieveAPIView

urlpatterns = [
    path('create/', EssayCreateAPIView.as_view(), name='essay_create'),
    path('letter/<int:pk>/content', LetterContentRetrieveAPIView.as_view()),
    path('<int:pk>/content', EssayContentRetrieveAPIView.as_view()),
]
