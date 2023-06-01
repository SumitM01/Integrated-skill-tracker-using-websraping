# from celery import shared_task
# from selenium import webdriver
# from docker import from_env

# @shared_task
# def scrape(url):
#     docker_client = from_env()
#     docker_client.containers.run("selenium/standalone-chrome", detach=True)
#     driver = webdriver.Remote(
#         command_executor='http://localhost:4444/wd/hub',
#         desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
#     driver.get(url)
#     # add your web scraping code here
#     driver.quit()
#     docker_client.containers.prune()

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .scraper import leetcode_contest,codechef_contest,spoj_contest,hackerrank_contest
from .models import Contest,Platform
from time import strftime, localtime
import requests


@shared_task
def scrape_hackerrank_contest():
    url = "https://www.hackerrank.com/contests"
    contests = hackerrank_contest(url)
    for contest in contests:
        print(contest)
        if not Contest.objects.filter(name=contest['name']):
            platform = Platform.objects.get(name=contest['platform'])
            create_hackerrank_contest = Contest.objects.create(platform=platform,
                                        name=contest['name'],
                                        date=contest['date'],
                                        time=contest['time'],
                                        duration=contest['duration'],
                                        status= contest['status'])
            create_hackerrank_contest.save()
        else:
            print("Contest already in database")
            
    
    return "done"


@shared_task
def scrape_codechef_contest():
    url = "https://www.codechef.com/contests"
    contests = codechef_contest(url)
    for contest in contests:
        print(contest)
        if not Contest.objects.filter(name=contest['name']):
            platform = Platform.objects.get(name=contest['platform'])
            create_codechef_contest = Contest.objects.create(platform=platform,
                                        name=contest['name'],
                                        date=contest['date'],
                                        time=contest['time'],
                                        duration=contest['duration'],
                                        status= contest['status'])
            create_codechef_contest.save()
        else:
            print("Contest already in database")
            
    
    return "done"


@shared_task
def scrape_leetcode_contest():
    url = "https://leetcode.com/contest/"
    contests = leetcode_contest(url)
    for contest in contests: 
        if not Contest.objects.filter(name=contest['name']):
            platform = Platform.objects.get(name=contest['platform'])
            contest_details = Contest.objects.create(platform=platform,
                                    name=contest['name'],
                                    date=contest['date'],
                                    time=contest['time'],
                                    duration=contest['duration'],
                                    status= contest['status'])
            contest_details.save()
        else:
            print(f"{contest['name']} already in database")
    
    return "done"

@shared_task
def scrape_spoj_contest():
    url = "https://www.spoj.com/contests"
    contests = spoj_contest(url)
    for contest in contests: 
        if not Contest.objects.filter(name=contest['name']):
            platform = Platform.objects.get(name=contest['platform'])
            contest_details = Contest.objects.create(platform=platform,
                                    name=contest['name'],
                                    date=contest['date'],
                                    time=contest['time'],
                                    duration=contest['duration'],
                                    status= contest['status'])
            contest_details.save()
        else:
            print(f"{contest['name']} already in database")
    
    return "done"

@shared_task
def scrape_codeforces_contest():
    url = "https://codeforces.com/api/contest.list"
    params = {
        "gym": False,
        "phase": "BEFORE",
        "from": 1,
        "count": 10
    }
    response = requests.get(url, params=params)
    contests = response.json()["result"]
    for contest in contests:
        if contest["phase"] == 'CODING' or contest["phase"] == 'BEFORE':
            platform = "Codeforces"
            name = f"{contest['name']}[{str(contest['id'])}]"
            start_date, start_time = strftime('%Y-%m-%d %H:%M:%S', localtime(contest['startTimeSeconds'])).split(" ")
            duration = str((contest['durationSeconds'] // 3600) // 24)+" days" if contest['durationSeconds'] // 3600 > 24 else str(contest['durationSeconds'] // 3600)+" hrs"
            print(platform, name, start_date, start_time, duration, contest['phase'])
            if not Contest.objects.filter(name=name):
                platform = Platform.objects.get(name=platform)
                contest_details = Contest.objects.create(platform=platform,
                                        name=name,
                                        date=start_date,
                                        time=start_time,
                                        duration=duration,
                                        status= 'upcoming')
                contest_details.save()
        else:
            print(f"{contest['name']} already in database")
    

    
    