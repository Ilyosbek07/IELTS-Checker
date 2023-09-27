from rest_framework import serializers
from apps.essay.models import Essay, Letter, Content, Recommend, Highlight, BaseEssay


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


class EssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Essay
        fields = (
            'html',
        )


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = (
            'html',
        )


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = (
            'essay',
            'letter',
            'main_type',
            'type',
            'note',
            'text',
        )


class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommend
        fields = (
            'name',
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
