from rest_framework import generics

from apps.essay.models import Letter, Essay
from apps.essay.serializers import CheckSerializer


class EssayCreateAPIView(generics.CreateAPIView):
    serializer_class = CheckSerializer

    def perform_create(self, serializer):
        essay_type = self.request.data['essay_type']
        if essay_type == 'essay':
            Essay.objects.create(
                html=self.request.data['html'],
                topic=self.request.data['topic']
            )
        elif essay_type == 'letter':
            Letter.objects.create(
                html=self.request.data['html'],
                topic=self.request.data['topic'],
                type=self.request.data['letter_type']
            )
