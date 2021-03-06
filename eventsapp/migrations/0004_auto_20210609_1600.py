# Generated by Django 3.2 on 2021-06-09 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0003_alter_eventmodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eventsapp.eventtypemodel'),
        ),
    ]
