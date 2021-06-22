from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Story, StoryFile, UserStoryFile

@api_view(['GET'])
def story_list(request, subs_id, project_id):
    stories = Story.objects.filter(project=project_id).values('preview', 'order_num', 'id')
    for i in stories:
        i['flag'] = len(UserStoryFile.objects.filter(is_watched=True, subs=subs_id)) ==\
                    len(UserStoryFile.objects.filter(subs=subs_id))

    return Response(data=stories)





def story_detail(request, subs_id):
    pass


