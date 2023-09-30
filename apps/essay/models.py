from django.db import models
from apps.common.models import BaseModel
from django.utils.translation import gettext as _

from apps.user.models import User

CHOICES = (
    ("Low", _("Low")),
    ("Not Enough", _("Not Enough")),
    ("Good", _("Good")),
)


class BaseEssay(BaseModel):
    # user = models.ForeignKey(
    #     User,
    #     related_name='user_essay',
    #     on_delete=models.CASCADE
    # )
    topic = models.TextField(_("Topic"), null=True, blank=True)
    text = models.TextField(_("Text"), null=True, blank=True)
    total_paragraph = models.IntegerField(verbose_name=_("Total Paragraphs"), null=True, blank=True)
    total_words = models.IntegerField(verbose_name=_("Total Words"), null=True, blank=True)
    average_sentence = models.IntegerField(verbose_name=_("Average Sentence"), null=True, blank=True)
    total_sentence = models.IntegerField(verbose_name=_("Total Sentences"), null=True, blank=True)
    cohesion = models.CharField(max_length=55, choices=CHOICES, verbose_name=_("Cohesion"), null=True, blank=True)
    sentence_variety = models.CharField(max_length=55, choices=CHOICES, verbose_name=_("Sentence Variety"), null=True,
                                        blank=True)
    spelling_mistakes = models.IntegerField(verbose_name=_("Spelling Mistakes"), null=True, blank=True)
    word_repetition = models.IntegerField(verbose_name=_("Word Repetition"), null=True, blank=True)

    class Meta:
        abstract = True


class Essay(BaseEssay):
    html = models.CharField(_("html"), max_length=255)

    class Meta:
        verbose_name = "Essay"
        verbose_name_plural = "Essays"

    def __str__(self):
        return self.topic  # You can choose a more suitable field to represent the object


class Letter(BaseEssay):
    html = models.TextField()

    class Type(models.TextChoices):
        formal = "formal", _("Formal")
        informal = "informal", _("InFormal")

    type = models.CharField(_("Type"), choices=Type.choices, max_length=125)

    class Meta:
        verbose_name = "Letter"
        verbose_name_plural = "Letters"

    def __str__(self):
        return self.topic  # You can choose a more suitable field to represent the object


class MainFeedbackChoices(models.TextChoices):
    feedback = "Feedback", _("Feedback")
    grammar = "Grammar", _("Grammar")
    tone_feedback = "Tone Feedback", _("Tone Feedback")
    lexical_resource = "Lexical Resource", _("Lexical Resource")
    report = "Report", _("Report")


class FeedbackChoices(models.TextChoices):
    feedback = "Feedback", _("Feedback")
    task_response = "Task Response", _("Task Response")
    cohesion_coherence = "Cohesion and Coherence", _("Cohesion and Coherence")
    spelling_mistakes = "Spelling Mistakes", _("Spelling Mistakes")
    word_repetition = "Word Repetition", _("Word Repetition")
    adjectives = "Adjectives", _("Adjectives")
    adverb = "Adverb", _("Adverb")
    vocabulary_suggestions = "Vocabulary Suggestions", _("Vocabulary Suggestions")
    compound_sentences = "Compound Sentences", _("Compound Sentences")
    correlative_sentences = "Correlative Sentences", _("Correlative Sentences")
    subordinate_clause = "Subordinate Clause", _("Subordinate Clause")
    grammatical_check = "Grammatical Check", _("Grammatical Check")


class Content(BaseModel):
    essay = models.ForeignKey(Essay,
                              on_delete=models.CASCADE,
                              null=True,
                              blank=True,
                              verbose_name=_("Essay")
                              )
    letter = models.ForeignKey(Letter,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               verbose_name=_("Letter")
                               )
    main_type = models.CharField(max_length=32,
                                 choices=MainFeedbackChoices.choices,
                                 null=True,
                                 blank=True,
                                 verbose_name=_("Main Type"))
    type = models.CharField(max_length=32,
                            choices=FeedbackChoices.choices,
                            null=True,
                            blank=True,
                            verbose_name=_("Type"))
    note = models.CharField(max_length=512, null=True, blank=True, verbose_name=_("Note"))
    text = models.TextField(verbose_name=_("Text"), null=True, blank=True)
    json = models.JSONField(verbose_name=_("Json"), null=True, blank=True)

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return f"Content {self.id}"  # You can choose a more suitable representation


class Recommend(BaseModel):
    text = models.CharField(max_length=256, verbose_name=_("Recommend text"))

    class Meta:
        verbose_name = "Recommend"
        verbose_name_plural = "Recommends"

    def __str__(self):
        return self.text  # You can choose a more suitable field to represent the object


class Highlight(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_("Content"))
    sentence = models.TextField(verbose_name=_("Sentence"))
    word = models.CharField(max_length=128, verbose_name=_("Word"))
    recommend = models.ManyToManyField(Recommend, blank=True, verbose_name=_("Recommend"))

    class Meta:
        verbose_name = "Highlight"
        verbose_name_plural = "Highlights"

    def __str__(self):
        return self.word
