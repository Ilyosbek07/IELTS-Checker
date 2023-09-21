from django.utils.translation import gettext as _
from apps.essay.models.essay import *  # Noqa
from apps.essay.models.latter import *  # Noqa


class Statistics(BaseModel):
    essay = models.ForeignKey(Essay, on_delete=models.CASCADE, related_name='essay_statistics', null=True, blank=True)
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE, related_name='letter_statistics', null=True,
                               blank=True)
    paragraph = models.IntegerField(verbose_name=_('Paragraphs'))
    words = models.IntegerField(verbose_name=_('Words'))
    average_sentence = models.IntegerField(verbose_name=_('Average Sentence Length'))
    COHESION_CHOICES = (
        ('good', _('Good')),
        ('not_enough', _('Not Enough')),
        ('len_55', _('Less than 55')),
    )
    cohesion = models.CharField(max_length=55, choices=COHESION_CHOICES, verbose_name=_('Cohesion'))
    sentence_variety = models.CharField(max_length=55, choices=COHESION_CHOICES, verbose_name=_('Sentence Variety'))
    spelling_mistakes = models.IntegerField(verbose_name=_('Spelling Mistakes'))
    word_repetition = models.IntegerField(verbose_name=_('Word Repetition'))

    class Meta:
        verbose_name = _('Statistics')
        verbose_name_plural = _('Statistics')
