from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.essay.models import Essay, Content, Letter
from apps.essay.open_ai.feedback import Feedback
from apps.essay.open_ai.lexical_grammar_check import Highlight


        # Content.objects.create(
        #     essay=instance,
        #     main_type='Feedback',
        #     note=feedback['tone_feedback']['note'],
        #     json=feedback['tone_feedback']
        # )
# @receiver(post_save, sender=Essay)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         print('boshlandi')
#         response_data = Highlight(
#             essay=instance.text
#         ).response()
#         feedback = Feedback(
#             essay=instance.text,
#             topic=instance.topic
#         ).response()
#
#         report = {
#             'cohesion_coherence': feedback['cohesion_coherence'],
#             "subordinating_clause": response_data['subordinating_clause'],
#             "compound_sentences": response_data['compound_sentences']
#         }
#         lexical_resource = {
#             "spelling_mistakes": response_data['spell_checker'],
#             "word_repetition": response_data['repetitive_words'],
#             "adverb": response_data['adverb'],
#             "adjective": response_data['adjective'],
#         }
#         Content.objects.create(
#             essay=instance,
#             main_type='Report',
#             note=feedback['cohesion_coherence']['note'],
#             json=report
#         )
#         Content.objects.create(
#             essay=instance,
#             main_type='Lexical Resource',
#             note='',
#             json=lexical_resource
#         )
#         Content.objects.create(
#             essay=instance,
#             main_type='Grammar',
#             note='',
#             json={'grammar_check': response_data['grammar_check']}
#         )
#
#         Content.objects.create(
#             essay=instance,
#             main_type='Tone Feedback',
#             note=feedback['tone_feedback']['note'],
#             json=feedback['tone_feedback']
#         )
#         # Content.objects.create(
#         #     essay=instance,
#         #     main_type='Feedback',
#         #     note=feedback['tone_feedback']['note'],
#         #     json=feedback['tone_feedback']
#         # )
