# Generated by Django 3.2.4 on 2021-06-24 08:23
import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_app', '0002_rename_story_storyfile_story_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstoryfile',
            name='watch_date',
            field=models.DateTimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
    ]
