from django.contrib import admin
from .models import Essay, Letter, Content, Recommend, Highlight


@admin.register(Essay)
class EssayAdmin(admin.ModelAdmin):
    list_display = ('topic', 'html')


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ('topic', 'html', 'type')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'essay', 'letter', 'main_type', 'type')


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('text',)


@admin.register(Highlight)
class HighlightAdmin(admin.ModelAdmin):
    list_display = ('content', 'sentence', 'word')

