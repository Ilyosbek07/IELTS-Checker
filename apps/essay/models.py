from django.db import models

from apps.common.models import BaseModel
from django.utils.translation import gettext as _


class BaseEssay(BaseModel):
    topic = models.TextField(_('Topic'))
    text = models.TextField(_('Text'))
    paragraph = models.IntegerField(verbose_name=_('Paragraphs'))
    words = models.IntegerField(verbose_name=_('Words'))
    average_sentence = models.IntegerField(verbose_name=_('Average Sentence Length'))
    COHESION_CHOICES = (
        ('low', _('Low')),
        ('Not Enough', _('Not Enough')),
        ('good', _('Good')),
    )
    cohesion = models.CharField(max_length=55, choices=COHESION_CHOICES, verbose_name=_('Cohesion'))
    sentence_variety = models.CharField(max_length=55, choices=COHESION_CHOICES, verbose_name=_('Sentence Variety'))
    spelling_mistakes = models.IntegerField(verbose_name=_('Spelling Mistakes'))
    word_repetition = models.IntegerField(verbose_name=_('Word Repetition'))


class aaa(BaseModel):
    class Choices(models.TextChoices):
        feedback = 'Feedback', _('Feedback')
        task_response = 'Task Response', _('Task Response')
        cohesion_coherence = 'Cohesion and Coherence', _('Cohesion and Coherence')
        lexical_resource = 'Lexical Resource', _('Lexical Resource')
        grammatical_range = 'Grammatical Range', _('Feedback')
        spelling_mistakes = 'Spelling Mistakes', _('Spelling Mistakes')
        word_repetition = 'Word Repetition', _('Word Repetition')
        adjectives = 'Adjectives', _('Adjectives')
        adverb = 'Adverb', _('Adverb')
        vocabulary_suggestions = 'Vocabulary Suggestions', _('Vocabulary Suggestions')
        compound_sentences = 'Compound Sentences', _('Compound Sentences')
        correlative_sentences = 'Correlative Sentences', _('Correlative Sentences')
        subordinate_clause = 'Subordinate Clause', _('Subordinate Clause')
        grammatical_check = 'Grammatical Check', _('Grammatical Check')


class Essay(BaseEssay):
    html = models.CharField(_('html'), max_length=255)

    class Meta:
        verbose_name = 'Essay'
        verbose_name_plural = 'Essays'


class Letter(BaseEssay):
    html = models.CharField(_('html'), max_length=255)

    class Type(models.TextChoices):
        formal = 'Formal', _('Formal')
        informal = 'InFormal', _('InFormal')

    type = models.CharField(_('Type'), max_length=125)

    class Meta:
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'
