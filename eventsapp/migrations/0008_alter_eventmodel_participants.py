# Generated by Django 3.2 on 2021-06-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0007_auto_20210609_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmodel',
            name='participants',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
