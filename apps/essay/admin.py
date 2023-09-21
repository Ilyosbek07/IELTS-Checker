from django.contrib import admin

from django.contrib import admin
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


# Custom admin class for Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'letter', 'desc')
    search_fields = ('letter__topic', 'desc')


# Custom admin class for TaskResponse
class TaskResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback', 'desc')
    search_fields = ('feedback__letter__topic', 'desc')


# Custom admin class for LexicalCheck
class LexicalCheckAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback', 'desc')
    search_fields = ('feedback__letter__topic', 'desc')


# Custom admin class for LexAnswer
class LexAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lex', 'sentence', 'word', 'notes')
    search_fields = ('lex__desc', 'sentence', 'word', 'notes')


# Custom admin class for Grammar
class GrammarAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback', 'desc')
    search_fields = ('feedback__letter__topic', 'desc')


# Custom admin class for GrammarAnswer
class GrammarAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'grammar', 'sentence', 'word', 'notes')
    search_fields = ('grammar__desc', 'sentence', 'word', 'notes')


# Custom admin class for Report
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'feedback', 'desc')
    search_fields = ('feedback__letter__topic', 'desc')


# Custom admin class for ReportAnswer
class ReportAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'report', 'sentence', 'word', 'notes')
    search_fields = ('report__desc', 'sentence', 'word', 'notes')


# Register your models with the custom admin classes
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(TaskResponse, TaskResponseAdmin)
admin.site.register(LexicalCheck, LexicalCheckAdmin)
admin.site.register(LexAnswer, LexAnswerAdmin)
admin.site.register(Grammar, GrammarAdmin)
admin.site.register(GrammarAnswer, GrammarAnswerAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(ReportAnswer, ReportAnswerAdmin)
