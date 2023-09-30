# Generated by Django 4.2.5 on 2023-09-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0008_alter_letter_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.CharField(blank=True, choices=[('Feedback', 'Feedback'), ('Task Response', 'Task Response'), ('Cohesion and Coherence', 'Cohesion and Coherence'), ('Spelling Mistakes', 'Spelling Mistakes'), ('Word Repetition', 'Word Repetition'), ('Adjectives', 'Adjectives'), ('Adverb', 'Adverb'), ('Vocabulary Suggestions', 'Vocabulary Suggestions'), ('Compound Sentences', 'Compound Sentences'), ('Correlative Sentences', 'Correlative Sentences'), ('Subordinate Clause', 'Subordinate Clause'), ('Grammatical Check', 'Grammatical Check')], max_length=32, null=True, verbose_name='Type'),
        ),
    ]
