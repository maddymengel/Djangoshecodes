from django.urls import path
from . import views
# from .views import profile_view
# from .views import stories_by_author

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name = 'story'), 
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    # path('author/<int:author_id>/', stories_by_author, name='stories_by_author')
]
