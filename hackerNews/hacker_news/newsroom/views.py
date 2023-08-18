from django.shortcuts import render

# Create your views here.
from .models import Story, Comments, Ask, askComments, Job
import requests 
from datetime import datetime, timedelta
import json
from requests.exceptions import ConnectionError
import schedule
import time
from .cron import my_scheduled_job
from django.views import generic

#Gets items from Hacker News Api and saves to database

#A loop that save the data below in a 5 minutes schedule

job = my_scheduled_job()

def index(request):
	"""View function for home page of site."""

	#Get tall top level data from db
	num_stories = Story.objects.all().count
	num_jobs = Job.objects.all().count
	num_asks = Ask.objects.all().count

	context = {
		'num_stories': num_stories,
		'num_jobs': num_jobs,
		'num_asks': num_asks,
	}

	# Render the HTML template index.html with the data in the context variable
	return render(request, 'index.html', context=context)


class StoryListView(generic.ListView):
    model = Story
    paginate_by = 10

class StoryDetailView(generic.DetailView):
    model = Story
    paginate = 10

class JobListView(generic.ListView):
    model = Job
    paginate_by = 10

class JobDetailView(generic.DetailView):
    model = Job
    paginate = 10

class AskListView(generic.ListView):
    model = Ask
    paginate_by = 10

class AskDetailView(generic.DetailView):
    model = Ask
    paginate = 10

def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        stories = Story.objects.filter(title__contains=search_query)
        return render(request, 'newsroom/result.html', {'query':search_query, 'stories':stories})
    else:
        return render(request, 'newsroom/result.html',{})