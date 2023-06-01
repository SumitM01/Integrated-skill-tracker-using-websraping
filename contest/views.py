from django.shortcuts import render
from .models import Contest
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import re
from django.utils import timezone
import pytz

@login_required
def home(request):
    # scrape_hackerrank_contest().datetime
    contests = Contest.objects.all()
    now = timezone.now()
    for contest in contests:
        contest_datetime = timezone.make_aware(datetime.combine(contest.date, contest.time))
        if contest.end_time is None:
            if contest.duration is not None : 
                duration_string = contest.duration.lower()
                match = re.search(r'(\d+(?:\.\d+)?)\s*(hour|hr|hrs|day|days|mths|months|mth|month)', duration_string)
                duration_unit = match.group(2)
                if duration_unit in ['hour', 'hr', 'hrs','hours']:
                    duration_value = float(match.group(1))
                    print(match.group(1),duration_value)
                    hours = int(duration_value)
                    minutes = int((duration_value - hours) * 60)
                    contest.end_time = contest_datetime + timedelta(hours=hours, minutes=minutes)
                elif duration_unit in ['day', 'days']:
                        duration_value = int(match.group(1))
                        contest.end_time = contest_datetime + timedelta(days=duration_value)
                elif duration_unit in ['month', 'months', 'mth', 'mths']:
                    duration_value = int(match.group(1))
                    contest.end_time = contest_datetime + timedelta(days=duration_value * 30)
                else:
                    contest.end_time = datetime(contest_datetime)
            else:
                contest.end_time = contest_datetime + timedelta(days=3650) 
        if contest.end_time < now:
            contest.status = 'expired'
        elif contest.duration is None or contest.end_time.astimezone(pytz.utc).replace(tzinfo=None) - contest_datetime.replace(tzinfo=None) > timedelta(days=30):
            contest.status = 'constant'
        elif contest_datetime <= now <= contest.end_time:
            contest.status = 'ongoing'
        elif contest_datetime > now:
            contest.status = 'upcoming'
        else:
            contest.status = 'expired'
        contest.save()
        ongoing_contest = Contest.objects.filter(status='ongoing')
    return render(request,'contest/contest.html',{'contest':contests})
