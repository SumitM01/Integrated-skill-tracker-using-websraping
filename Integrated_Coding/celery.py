from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from kombu import Queue, Exchange

os.environ.setdefault("DJANGO_SETTINGS_MODULE","Integrated_Coding.settings")

app = Celery("Integrated_Coding")
app.conf.enable_utc=False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object("django.conf:settings",namespace="CELERY")

def map_priority(priority):
    # Map a priority value in the range 1-10 to the Celery priority range of 0-255
    return int(priority * (255 / 10))

CELERY_QUEUES = (
    Queue('high_priority', Exchange('high_priority'), routing_key='high_priority'),
    Queue('medium_priority', Exchange('medium_priority'), routing_key='medium_priority'),
     Queue('low_priority', Exchange('low_priority'), routing_key='low_priority'),
)

app.conf.beat_schedule = {
    'task-1': {
        'task': 'contest.tasks.scrape_codechef_contest',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'high_priority',
            'priority': map_priority(10) # Map priority value of 10 to Celery priority range
        }
    },
    'task-2' : {
        'task': 'contest.tasks.scrape_leetcode_contest',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'high_priority',
            'priority': map_priority(10) # Map priority value of 10 to Celery priority range
        }
    },
    'task-3' : {
        'task': 'contest.tasks.scrape_spoj_contest',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'high_priority',
            'priority': map_priority(10) # Map priority value of 10 to Celery priority range
        }
    },
    'task-4' : {
        'task': 'coding_profile.tasks.scrape_leetcode_profile',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'medium_priority',
            'priority': map_priority(5) # Map priority value of 10 to Celery priority range
        }
    },
    'task-5' : {
        'task': 'coding_profile.tasks.scrape_codeforces_profile',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'medium_priority',
            'priority': map_priority(5) # Map priority value of 10 to Celery priority range
        }
    },
    'task-6' : {
        'task': 'coding_profile.tasks.scrape_codechef_profile',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'medium_priority',
            'priority': map_priority(5) # Map priority value of 10 to Celery priority range
        }
    },
    'task-7' : {
        'task': 'contest.tasks.scrape_hackerrank_contest',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'high_priority',
            'priority': map_priority(10) # Map priority value of 10 to Celery priority range
        }
    },
    'task-8' : {
        'task': 'coding.tasks.update_leaderboard',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'low_priority',
            'priority': map_priority(1) # Map priority value of 10 to Celery priority range
        }
    },
    'task-9': {
        'task': 'contest.tasks.scrape_codeforces_contest',
        'schedule': 200.0, # every hour
        'args': (),
        'options': {
            'queue': 'high_priority',
            'priority': map_priority(10) # Map priority value of 10 to Celery priority range
        }
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')