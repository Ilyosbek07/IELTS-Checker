# Generated by Django 4.2.5 on 2023-09-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0007_alter_content_main_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='html',
            field=models.TextField(),
        ),
    ]