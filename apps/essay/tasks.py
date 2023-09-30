from celery import shared_task

from apps.essay.models import Content
from apps.essay.open_ai.feedback import Feedback
from apps.essay.open_ai.lexical_grammar_check import Highlight
from apps.essay.open_ai.statistics import EssayAnalyzer


@shared_task
def add(x, y):
    return x + y


@shared_task
def create_highlight(instance, created, text, topic):
    if created:
        response_data = EssayAnalyzer(
            essay=text,
            topic=topic
        ).response()
        feedback = Feedback(
            essay=text,
            topic=topic
        ).response()
        report = {
            'cohesion_and_coherence': feedback[0],
            "subordinating_clause": response_data['subordinating_clause'],
            "compound_sentences": response_data['compound_sentences']
        }
        lexical_resource = {
            "spelling_mistakes": response_data['spell_checker'],
            "word_repetition": response_data['repetitive_words'],
            "adverb": response_data['adverb'],
            "adjective": response_data['adjective'],
        }
        Content.objects.bulk_create([
            Content(letter_id=instance,main_type='Lexical Resource',type='',note=''),
            Content(letter_id=instance,main_type='Grammar',type='',note=''),
            Content(letter_id=instance,main_type='Tone Feedback',type='',note=feedback[1]['note']),
            Content(letter_id=instance,main_type='Report',type='',note=''),
        ])
        Content.objects.create(
            letter_id=instance,
            main_type='Lexical Resource',
            note='',
            json=lexical_resource
        )
        Content.objects.create(
            letter_id=instance,
            main_type='Grammar',
            note='',
            json={'grammar_check': response_data['grammar_check']}
        )
        print(feedback[1]['note'])
        Content.objects.create(
            letter_id=instance,
            main_type='Tone Feedback',
            note=feedback[1]['note'],
            json=feedback[1]
        )
