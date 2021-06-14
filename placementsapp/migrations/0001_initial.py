# Generated by Django 3.2 on 2021-06-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlacementsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='company_logos/')),
                ('company_name', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('students', models.JSONField(default=list)),
            ],
        ),
    ]
