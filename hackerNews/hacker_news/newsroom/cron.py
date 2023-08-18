from django_cron import CronJobBase, Schedule
import requests
from .models import Story, Comments, Ask, askComments, Job
from datetime import datetime, timedelta
import json
from requests.exceptions import ConnectionError
import schedule
import time

def my_scheduled_job():
    new_stroies_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    response = requests.get(new_stroies_url)
    latest_news = response.text.split(',')[1:len(response.text.split(','))-2]
    last_news = response.text.split(',')[-1]
    latest_news.insert(len(last_news), last_news.strip().split()[0])

    latest_100 = 400
    res = [int(x.strip()) for x in latest_news[latest_100+1:latest_100+10]]

       # loops through the list of 100 stories id, then send a new get request to get individual item and save to database
    try:
        for item_id in res:
            resp = requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
                                .format(item_id))

            if resp.status_code == 200:
                data = resp.json()

                # stores the new story data in the Story class in the models.py file
                for key, value in data.items():
                    stories = Story(
                        story_id=data['id'],
                        story_type=data['type'],
                        by=data['by'],
                        time=datetime.now(),
                        descendant=data['descendants'],
                        score=data['score'],
                        title=data['title'],
                        url=data['url'],
                        # kids = data['kids']
                        )
                    saved = stories.save()

                    if data['kids']:
                        kids_id = data['kids']
                        for kid_id in kids_id:
                            kid_req = requests.get(
                                'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(kid_id))

                            if kid_req.status_code == 200:
                                kid_data = kid_req.json()

                                # capture each comment data and store to database
                                for key, value in kid_data.items():
                                    comments = Comments(
                                        by=kid_data['by'],
                                        comment_id=kid_data['id'],
                                        text=kid_data['text'],
                                        time=datetime.now(),
                                        comment_type=kid_data['type'],
                                        parent=kid_data['parent']
                                        )

                                    saved = comments.save()
    except KeyError:
        print("Unexpected Error Occurred!")

    except ConnectionError as e:
        print(e)

    job_arr = []
    job_items_id = 'https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty'
    job_res = requests.get(job_items_id).json()
    job_arr = job_res[:]

    try:
        for job_id in job_arr:
            resp = requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
                                .format(job_id))

            if resp.status_code == 200:
                j_data = resp.json()

                # stores the new story data in the Story class in the models.py file
                for key, value in j_data.items():
                    j = Job(
                        job_id = j_data['id'],
                        item_type = j_data['type'],
                        by = j_data['by'],
                        time = datetime.now(),
                        score = j_data['score'],
                        title = j_data['title'],
                        url = j_data['url'],
                        )
                    j.save()
    except KeyError:
        print("Unexpected Error Occurred!")

    except ConnectionError as e:
        print(e)

    # Get the list of ask item ids
    ask_arr = []
    ask_item_id = 'https://hacker-news.firebaseio.com/v0/askstories.json?print=pretty'
    ask_res = requests.get(ask_item_id).json()
    ask_arr = ask_res[:]

    try:
        for a_id in ask_arr:
            a_res = requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
                                 .format(item_id))

            if a_res.status_code == 200:
                a_data = a_res.json()

                # stores the new story data in the Story class in the models.py file
                for key, value in a_data.items():
                    a = Ask(
                        ask_id = a_data['id'],
                        item_type = a_data['type'],
                        by = a_data['by'],
                        time = datetime.now(),
                        descendant = a_data['descendants'],
                        score = a_data['score'],
                        title = a_data['title'],
                        )
                    saved = a.save()

                    if a_data['kids']:
                        a_kids_id = a_data['kids']
                        for a_kid_id in a_kids_id:
                            a_kid_req = requests.get('https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(a_kid_id))

                            if a_kid_req.status_code == 200:
                                a_kid_data = a_kid_req.json()

                                # capture each comment data and store to database
                                for key, value in a_kid_data.items():
                                    a_comments = askComments(
                                        by = a_kid_data['by'],
                                        comment_id = a_kid_data['id'],
                                        text = a_kid_data['text'],
                                        time = datetime.now(),
                                        comment_type =  a_kid_data['type'],
                                        parent = a_kid_data['parent']
                                        )

                                    saved = a_comments.save()
    except KeyError:
        print("Unexpected Error Occurred!")

    except ConnectionError as e:
        print(e)

    except TypeError as err:
        print(err)
