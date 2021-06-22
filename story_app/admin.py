from django.contrib import admin

# Register your models here.
from .models import Projects, Story, StoryFile, UserStoryFile, Subscribers

admin.site.register(Projects)
admin.site.register(Story)
admin.site.register(StoryFile)
admin.site.register(UserStoryFile)
admin.site.register(Subscribers)

