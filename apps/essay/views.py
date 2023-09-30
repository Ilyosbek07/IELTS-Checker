from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

# import checker
from apps.essay.models import Letter, Essay, Content
from apps.essay.open_ai.statistics import EssayAnalyzer
from apps.essay.serializers import CheckSerializer, LetterStatisticsSerializer, EssayStatisticsSerializer, \
    LetterContentSerializer, EssayContentSerializer
from apps.essay.tasks import create_highlight
from utils import clean_html_codes


class EssayStatisticsRetrieveAPIView(generics.ListAPIView):
    queryset = Essay.objects.all()
    serializer_class = EssayStatisticsSerializer


class EssayCreateAPIView(APIView):

    def post(self, request):
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid():
            data = request.data
            cleaned_text = clean_html_codes(
                text=data['html']
            )
            analyze = EssayAnalyzer(
                topic=data['topic'],
                essay=cleaned_text
            )
            analyzed_data = analyze.analyze_essay()
            analyzed_data['html'] = data['html']
            analyzed_data['spelling_mistakes'] = len(analyzed_data['spelling_mistakes'])
            analyzed_data['word_repetition'] = len(analyzed_data['word_repetition'])
            essay_type = data['essay_type']
            if essay_type == 'ielts':
                Essay.objects.create(
                    html=data['html'],
                    topic=data['topic'],
                    text=cleaned_text,
                    total_paragraph=analyzed_data['total_paragraph'],
                    spelling_mistakes=analyzed_data['spelling_mistakes'],
                    total_sentence=analyzed_data['total_sentence'],
                    total_words=analyzed_data['total_words'],
                    average_sentence=analyzed_data['average_sentence'],
                    cohesion=analyzed_data['cohesion_and_sentence_variety']['response'][0]['cohesion'],
                    sentence_variety=analyzed_data['cohesion_and_sentence_variety']['response'][1]['sentence_variety'],
                    word_repetition=analyzed_data['word_repetition'],
                )
                return Response(data=analyzed_data, status=status.HTTP_201_CREATED)
            elif essay_type == 'letter':
                instance = Letter.objects.create(
                    html=data['html'],
                    topic=data['topic'],
                    type=data['letter_type'],
                    text=cleaned_text,
                    total_paragraph=analyzed_data['total_paragraph'],
                    spelling_mistakes=analyzed_data['spelling_mistakes'],
                    total_sentence=analyzed_data['total_sentence'],
                    total_words=analyzed_data['total_words'],
                    average_sentence=analyzed_data['average_sentence'],
                    cohesion=analyzed_data['cohesion_and_sentence_variety']['response'][0]['cohesion'],
                    sentence_variety=analyzed_data['cohesion_and_sentence_variety']['response'][1]['sentence_variety'],
                    word_repetition=analyzed_data['word_repetition'],
                )
                analyzed_data['id'] = instance.id
                create_highlight.delay(
                    instance=instance.id,
                    created=True,
                    text=cleaned_text,
                    topic=data['topic'])
                return Response(data=analyzed_data, status=status.HTTP_201_CREATED)

    class LetterContentRetrieveAPIView(generics.ListAPIView):
        queryset = Content.objects.all()
        serializer_class = LetterContentSerializer

        def get_queryset(self):
            pk = self.kwargs.get("pk")
            return Content.objects.filter(letter=pk)


class LetterContentRetrieveAPIView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = LetterContentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Content.objects.filter(letter=pk)


class EssayContentRetrieveAPIView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = EssayContentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Content.objects.filter(essay=pk)
