# Generated by Django 4.2.5 on 2023-09-27 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "main_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Lexical Resource", "Lexical Resource"),
                            ("Grammatical Range", "Feedback"),
                        ],
                        max_length=32,
                        null=True,
                        verbose_name="Main Type",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Feedback", "Feedback"),
                            ("Task Response", "Task Response"),
                            ("Cohesion and Coherence", "Cohesion and Coherence"),
                            ("Spelling Mistakes", "Spelling Mistakes"),
                            ("Word Repetition", "Word Repetition"),
                            ("Adjectives", "Adjectives"),
                            ("Adverb", "Adverb"),
                            ("Vocabulary Suggestions", "Vocabulary Suggestions"),
                            ("Compound Sentences", "Compound Sentences"),
                            ("Correlative Sentences", "Correlative Sentences"),
                            ("Subordinate Clause", "Subordinate Clause"),
                            ("Grammatical Check", "Grammatical Check"),
                        ],
                        max_length=32,
                        verbose_name="Type",
                    ),
                ),
                (
                    "note",
                    models.CharField(
                        blank=True, max_length=512, null=True, verbose_name="Note"
                    ),
                ),
                ("text", models.TextField(blank=True, null=True, verbose_name="Text")),
            ],
            options={
                "verbose_name": "Content",
                "verbose_name_plural": "Contents",
            },
        ),
        migrations.CreateModel(
            name="Essay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "topic",
                    models.TextField(blank=True, null=True, verbose_name="Topic"),
                ),
                ("text", models.TextField(blank=True, null=True, verbose_name="Text")),
                (
                    "total_paragraph",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Total Paragraphs"
                    ),
                ),
                (
                    "total_words",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Total Words"
                    ),
                ),
                (
                    "average_sentence",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Average Sentence"
                    ),
                ),
                (
                    "total_sentence",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Total Sentences"
                    ),
                ),
                (
                    "cohesion",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("low", "Low"),
                            ("Not Enough", "Not Enough"),
                            ("good", "Good"),
                        ],
                        max_length=55,
                        null=True,
                        verbose_name="Cohesion",
                    ),
                ),
                (
                    "sentence_variety",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("low", "Low"),
                            ("Not Enough", "Not Enough"),
                            ("good", "Good"),
                        ],
                        max_length=55,
                        null=True,
                        verbose_name="Sentence Variety",
                    ),
                ),
                (
                    "spelling_mistakes",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Spelling Mistakes"
                    ),
                ),
                (
                    "word_repetition",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Word Repetition"
                    ),
                ),
                ("html", models.CharField(max_length=255, verbose_name="html")),
            ],
            options={
                "verbose_name": "Essay",
                "verbose_name_plural": "Essays",
            },
        ),
        migrations.CreateModel(
            name="Letter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "topic",
                    models.TextField(blank=True, null=True, verbose_name="Topic"),
                ),
                ("text", models.TextField(blank=True, null=True, verbose_name="Text")),
                (
                    "total_paragraph",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Total Paragraphs"
                    ),
                ),
                (
                    "total_words",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Total Words"
                    ),
                ),
                (
                    "average_sentence",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Average Sentence"
                    ),
                ),
                (
                    "total_sentence",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Total Sentences"
                    ),
                ),
                (
                    "cohesion",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("low", "Low"),
                            ("Not Enough", "Not Enough"),
                            ("good", "Good"),
                        ],
                        max_length=55,
                        null=True,
                        verbose_name="Cohesion",
                    ),
                ),
                (
                    "sentence_variety",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("low", "Low"),
                            ("Not Enough", "Not Enough"),
                            ("good", "Good"),
                        ],
                        max_length=55,
                        null=True,
                        verbose_name="Sentence Variety",
                    ),
                ),
                (
                    "spelling_mistakes",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Spelling Mistakes"
                    ),
                ),
                (
                    "word_repetition",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Word Repetition"
                    ),
                ),
                ("html", models.CharField(max_length=255, verbose_name="html")),
                ("type", models.CharField(max_length=125, verbose_name="Type")),
            ],
            options={
                "verbose_name": "Letter",
                "verbose_name_plural": "Letters",
            },
        ),
        migrations.CreateModel(
            name="Recommend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "text",
                    models.CharField(max_length=256, verbose_name="Recommend text"),
                ),
            ],
            options={
                "verbose_name": "Recommend",
                "verbose_name_plural": "Recommends",
            },
        ),
        migrations.CreateModel(
            name="Highlight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                ("sentence", models.TextField(verbose_name="Sentence")),
                ("word", models.CharField(max_length=128, verbose_name="Word")),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="essay.content",
                        verbose_name="Content",
                    ),
                ),
                (
                    "recommend",
                    models.ManyToManyField(
                        blank=True, to="essay.recommend", verbose_name="Recommend"
                    ),
                ),
            ],
            options={
                "verbose_name": "Highlight",
                "verbose_name_plural": "Highlights",
            },
        ),
        migrations.AddField(
            model_name="content",
            name="essay",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="essay.essay",
                verbose_name="Essay",
            ),
        ),
        migrations.AddField(
            model_name="content",
            name="letter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="essay.letter",
                verbose_name="Letter",
            ),
        ),
    ]
