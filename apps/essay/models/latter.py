from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from apps.common.models import BaseModel


class Letter(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_letters')
    topic = models.CharField(max_length=255, verbose_name=_('Topic'))
    text = models.TextField()
    TYPE_CHOICES = (
        ('formal', _('Formal')),
        ('informal', _('Informal')),
    )
    type = models.CharField(max_length=55, choices=TYPE_CHOICES, verbose_name=_('Type'))

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = _('Letter')
        verbose_name_plural = _('Letters')


from django.db import models
from django.utils.translation import gettext as _


class Feedback(BaseModel):
    letter = models.ForeignKey('Letter', on_delete=models.CASCADE, related_name='letter_feedback')
    desc = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f"Feedback for Letter: {self.letter}"

    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedback')


class TaskResponse(BaseModel):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='t_res_feedback')
    desc = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f"Task Response for Feedback: {self.feedback}"

    class Meta:
        verbose_name = _('Task Response')
        verbose_name_plural = _('Task Responses')


class LexicalCheck(BaseModel):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='lex_check_feedback')
    desc = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f"Lexical Check for Feedback: {self.feedback}"

    class Meta:
        verbose_name = _('Lexical Check')
        verbose_name_plural = _('Lexical Checks')


class LexAnswer(BaseModel):
    lex = models.ForeignKey(LexicalCheck, on_delete=models.CASCADE, related_name='lex_answer')
    sentence = models.TextField(verbose_name=_('Sentence'))
    word = models.TextField(verbose_name=_('Word'))
    notes = models.CharField(max_length=125, choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2')],
                             verbose_name=_('Notes'))

    def __str__(self):
        return f"Lexical Answer for Lexical Check: {self.lex}"

    class Meta:
        verbose_name = _('Lexical Answer')
        verbose_name_plural = _('Lexical Answers')


class Grammar(BaseModel):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='grammar_feedback')
    desc = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f"Grammar for Feedback: {self.feedback}"

    class Meta:
        verbose_name = _('Grammar')
        verbose_name_plural = _('Grammar')


class GrammarAnswer(BaseModel):
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE, related_name='grammar_answer')
    sentence = models.TextField(verbose_name=_('Sentence'))
    word = models.TextField(verbose_name=_('Word'))
    notes = models.CharField(max_length=125, choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2')],
                             verbose_name=_('Notes'))

    def __str__(self):
        return f"Grammar Answer for Grammar Check: {self.grammar}"

    class Meta:
        verbose_name = _('Grammar Answer')
        verbose_name_plural = _('Grammar Answers')


class Report(BaseModel):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE, related_name='report_feedback')
    desc = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return f"Report for Feedback: {self.feedback}"

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')


class ReportAnswer(BaseModel):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='report_answer')
    sentence = models.TextField(verbose_name=_('Sentence'))
    word = models.TextField(verbose_name=_('Word'))
    notes = models.CharField(max_length=125, choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2')],
                             verbose_name=_('Notes'))

    def __str__(self):
        return f"Report Answer for Report: {self.report}"

    class Meta:
        verbose_name = _('Report Answer')
        verbose_name_plural = _('Report Answers')
