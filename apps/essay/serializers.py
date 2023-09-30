from rest_framework import serializers
from apps.essay.models import Essay, Letter, Content, Recommend, Highlight, BaseEssay


class CheckSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    html = serializers.CharField()
    topic = serializers.CharField()
    essay_type = serializers.CharField()
    letter_type = serializers.CharField()


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


class EssayStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Essay
        fields = (
            'html',
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


class LetterStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = (
            'html',
            'text',
            'type',
            'total_paragraph',
            'total_words',
            'average_sentence',
            'total_sentence',
            'cohesion',
            'sentence_variety',
            'spelling_mistakes',
            'word_repetition',
        )


class LetterContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            'letter',
            'main_type',
            'note',
            'text',
            'json',
        )


class EssayContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            'essay',
            'main_type',
            'note',
            'text',
            'json',
        )
