# Generated by Django 3.2 on 2021-06-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievementsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievementmodel',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]