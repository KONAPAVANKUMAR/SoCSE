# Generated by Django 3.2 on 2021-06-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0005_auto_20210609_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventmodel',
            name='participants',
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='participants',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
    ]
