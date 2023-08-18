from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('stories/', views.StoryListView.as_view(), name='story'),
	path('story/<int:pk>', views.StoryDetailView.as_view(), name='story-detail'),
	path('jobs/', views.JobListView.as_view(), name='job'),
	path('job/<int:pk>', views.JobDetailView.as_view(), name='job-detail'),
	path('asks/', views.AskListView.as_view(), name='ask'),
	path('ask/<int:pk>', views.AskDetailView.as_view(), name='ask-detail'),
	path('search/', views.search_feature, name='search-view'),
]