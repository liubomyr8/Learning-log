# Generated by Django 4.2.5 on 2023-09-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
