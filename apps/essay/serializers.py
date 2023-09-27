from rest_framework import serializers
from apps.essay.models import Essay, Letter, Content, Recommend, Highlight, BaseEssay


class CheckSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    html = serializers.CharField(max_length=255)
    topic = serializers.CharField(max_length=255)
    essay_type = serializers.CharField(max_length=55)
    letter_type = serializers.CharField(max_length=55, allow_null=True, allow_blank=True)


class BaseEssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseEssay
        fields = (
            'topic',
            'text',
            'total_paragraph',
            'total_words',
            'average_sentence',
            'total_sentence',
            'cohesion',
            'sentence_variety',
            'spelling_mistakes',
            'word_repetition',
        )


class HighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Highlight
        fields = (
            'content',
            'sentence',
            'word',
            'recommend',
        )
