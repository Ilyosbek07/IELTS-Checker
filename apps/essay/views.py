from rest_framework import generics

from apps.essay.models import Letter, Essay, BaseEssay
from apps.essay.serializers import CheckSerializer, LetterStatisticsSerializer, EssayStatisticsSerializer


class LetterListAPIView(generics.ListAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterStatisticsSerializer
class LetterRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Letter.objects.all()
    serializer_class = LetterStatisticsSerializer


class EssayStatisticsListAPIView(generics.ListAPIView):
    queryset = Essay.objects.all()
    serializer_class = EssayStatisticsSerializer
class EssayStatisticsRetrieveAPIView(generics.ListAPIView):
    queryset = Essay.objects.all()
    serializer_class = EssayStatisticsSerializer


class EssayCreateAPIView(generics.CreateAPIView):
    serializer_class = CheckSerializer

    def perform_create(self, serializer):
        essay_type = self.request.data['essay_type']
        if essay_type == 'essay':
            Essay.objects.create(
                user=self.request.user,
                html=self.request.data['html'],
                topic=self.request.data['topic']
            )
        elif essay_type == 'letter':
            Letter.objects.create(
                user=self.request.user,
                html=self.request.data['html'],
                topic=self.request.data['topic'],
                type=self.request.data['letter_type']
            )
