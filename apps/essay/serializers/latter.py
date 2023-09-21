from rest_framework import serializers
from apps.essay.models.latter import (
    Feedback,
    TaskResponse,
    LexicalCheck,
    LexAnswer,
    Grammar,
    GrammarAnswer,
    Report,
    ReportAnswer
)


class LexAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LexAnswer
        fields = (
            'lex',
            'sentence',
            'word',
            'notes'
        )


class LexicalCheckSerializer(serializers.ModelSerializer):
    lex_answer = LexAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = LexicalCheck
        fields = (
            'feedback',
            'desc',
            'lex_answer',
        )


class GrammarAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrammarAnswer
        fields = (
            'sentence',
            'word',
            'notes',
        )


class GrammarSerializer(serializers.ModelSerializer):
    grammar_answer = GrammarAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Grammar
        fields = (
            'feedback',
            'desc',
            'grammar_answer',
        )


class ReportAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportAnswer
        fields = (
            'sentence',
            'word',
            'notes',
        )


class ReportSerializer(serializers.ModelSerializer):
    report_answer = ReportAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = (
            'feedback',
            'desc',
            'report_answer',
        )


class TaskResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResponse
        fields = (
            'feedback',
            'desc',
        )


class FeedbackSerializer(serializers.ModelSerializer):
    task_response = TaskResponseSerializer(many=True, read_only=True)
    lexical_check = LexicalCheckSerializer(many=True, read_only=True)
    grammar = GrammarSerializer(many=True, read_only=True)
    report = ReportSerializer(many=True, read_only=True)

    class Meta:
        model = Feedback
        fields = (
            'letter',
            'desc',
            'task_response',
            'lexical_check',
            'grammar',
            'report',
        )
class Serializer(serializers.ModelSerializer):
    pass