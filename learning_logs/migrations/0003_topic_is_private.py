# Generated by Django 4.2.5 on 2023-11-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_alter_topic_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]