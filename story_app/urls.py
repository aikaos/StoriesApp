from django.urls import path
from . import views


urlpatterns = [
    path('story/all/<int:subs_id>/<int:project_id>/', views.story_list),
    path('story/file/<int:subs_id>/<int:story_id>/', views.story_detail)
]