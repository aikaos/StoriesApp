from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Story, StoryFile, UserStoryFile


@api_view(['GET'])
def story_list(request, subs_id, project_id):
    """
    it's been watched all story with all files
    """
    stories = Story.objects.filter(project=project_id).values('preview', 'order_num', 'id')
    for i in stories:
        i['flag'] = len(UserStoryFile.objects.filter(is_watched=True, subs=subs_id)) ==\
                    len(UserStoryFile.objects.filter(subs=subs_id)) #TODO

    return Response(data=stories)

@api_view(['GET'])
def story_detail(request, subs_id, story_id):
    queryset_story_files = StoryFile.objects.filter(pk=story_id).values('moreDetailedUrl', 'moreDetailedText',
                                                                        'content_type', 'content_url', 'duration')

    queryset_user_story_files = UserStoryFile.objects.filter(pk=story_id, #TODO
                                                             subs=subs_id).values('is_watched').values()
    if queryset_story_files:
        return Response(data=list(queryset_story_files) + list(queryset_user_story_files))
    return Response(status=404)


