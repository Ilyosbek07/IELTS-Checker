# Generated by Django 4.2.5 on 2023-09-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0005_content_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='type',
        ),
        migrations.AlterField(
            model_name='content',
            name='main_type',
            field=models.CharField(blank=True, choices=[('Feedback', 'Feedback'), ('Grammar', 'Grammar'), ('Tone Feedback', 'Tone Feedback'), ('Lexical Resource', 'Lexical Resource'), ('Grammatical Range', 'Feedback')], max_length=32, null=True, verbose_name='Main Type'),
        ),
    ]