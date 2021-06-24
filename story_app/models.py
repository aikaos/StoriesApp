from django.db import models
from datetime import time
# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Story(models.Model):
    preview = models.ImageField(upload_to='img/story/preview')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    add_date = models.DateTimeField(auto_now_add=True)
    order_num = models.IntegerField()
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)


class StoryFile(models.Model):
    moreDetailedUrl = models.SlugField()
    moreDetailedText = models.CharField(max_length=200)
    content_type = models.CharField(max_length=50)
    content_url = models.SlugField()
    duration = models.TimeField(default=time(second=15))
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    story_id = models.ForeignKey(Story, on_delete=models.DO_NOTHING)


class UserStoryFile(models.Model):
    story_file = models.ForeignKey(StoryFile, on_delete=models.DO_NOTHING)
    subs = models.ForeignKey('Subscribers', on_delete=models.DO_NOTHING)
    is_watched = models.BooleanField()
    watch_date = models.DateTimeField()


class Subscribers(models.Model):
    subs_id = models.BigIntegerField(primary_key=True)

