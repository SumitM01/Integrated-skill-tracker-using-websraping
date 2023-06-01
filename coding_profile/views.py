from django.shortcuts import render
from .models import LeaderBoard,CodechefDetails,HackerRankDetails,CodeforcesDetails,SpojDetails,LeetcodeDetails
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .tasks import scrape_codechef_profile,scrape_leetcode_profile,scrape_codeforces_profile,update_leaderboard

@login_required
def stat(request):
    # scrape_leetcode_profile()
    return render(request,'coding_profile/stat.html')

@login_required
def leaderboard(request):
    update_leaderboard()
    if request.POST:
        institute=request.POST.get('institute-name')
        print(institute)
    else:
        institute='Global'
    leaderboard = LeaderBoard.objects.all()
    return render(request, 'coding_profile/leaderboard.html',{'leaderboard':leaderboard, 'institute':institute})

