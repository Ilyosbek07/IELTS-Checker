# Generated by Django 4.2.5 on 2023-09-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_alter_subscription_extra_info_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='extra_info',
            field=models.ManyToManyField(related_name='extra_info', to='subscription.extrainfo', verbose_name='Extra info'),
        ),
    ]