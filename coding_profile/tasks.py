from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.contrib.auth.models import User
from .models import LeetcodeDetails,PlatformID,CodechefDetails,CodeforcesDetails,LeaderBoard,SpojDetails,HackerRankDetails
from .scraper import leetcode_profile,codechef_profile
import requests

@shared_task
def scrape_hackerrank_profile():
    return "done"

@shared_task
def scrape_codechef_profile():
    users = User.objects.all() # type: ignore
    for user in users:
        try:
            codechefid = PlatformID.objects.get(user=user).codechefID
            if codechefid:
                url = f"https://www.codechef.com/users/{codechefid}"
                codechef_details = codechef_profile(url)
                print(codechef_details)
                user_codechef_details = CodechefDetails.objects.get(user=user)
                user_codechef_details.rank = codechef_details['rank']
                user_codechef_details.no_of_contest_attempted = codechef_details['contest_attempted']
                user_codechef_details.contest_rating = codechef_details['contest_rating']
                user_codechef_details.no_of_problem_solved= codechef_details['problem_solved']
                user_codechef_details.score = int(float(codechef_details['contest_rating'])*float(codechef_details['contest_attempted']//2)*0.5+float(codechef_details['problem_solved'])*5 ) 
                user_codechef_details.save() 
        except Exception as e:
            print("codechef profile doesn't exist",e)
    return "done"

@shared_task
def scrape_codeforces_profile():
        users = User.objects.all() # type: ignore
        for user in users:
            try:
                codeforcesid =PlatformID.objects.get(user=user).codeforcesID
                user_codeforces_details = CodeforcesDetails.objects.get(user=user)
                if codeforcesid:
                    user_api_url = "https://codeforces.com/api/user.info"
                    problem_api_url = "https://codeforces.com/api/user.status"
                    contest_api_url = "https://codeforces.com/api/user.rating"
                    user_params = {"handles": codeforcesid }
                    pc_params = {"handle": codeforcesid}
                    problem_response = requests.get(problem_api_url, params=pc_params)
                    contest_response = requests.get(contest_api_url, params=pc_params)
                    user_response = requests.get(user_api_url, params=user_params)
                    
                    if user_response.json()["status"] == "FAILED" or problem_response.json()["status"] == "FAILED" or contest_response.json()["status"] == "FAILED":
                        print("User:",user_response.json()["status"],"Problem:",problem_response.json()["status"],"Contest:",contest_response.json()["status"])
                    else:
                        user_data = user_response.json()["result"][0]
                        problem_data = problem_response.json()["result"]
                        contest_data = contest_response.json()["result"]
                        problems_solved = 0
                        for obj in problem_data:
                            if obj["verdict"] == "OK":
                                problems_solved += 1
                        codeforces_details ={
                            "handle": user_data["handle"],
                            "rank": user_data["rank"],
                            "rating": user_data["rating"],
                            "contest_attended": len(contest_data),
                            "questions_solved": problems_solved
                        }

                        # store the details in the database object
                        user_codeforces_details.rank = codeforces_details['rank']
                        user_codeforces_details.no_of_contest_attempted = codeforces_details['contest_attended']
                        user_codeforces_details.contest_rating = codeforces_details['rating']
                        user_codeforces_details.no_of_problem_solved= codeforces_details['questions_solved']
                        user_codeforces_details.score = int(float(codeforces_details['rating'])*float(codeforces_details['contest_attended']//2)*0.5+float(codeforces_details['questions_solved'])*5 ) 
                        user_codeforces_details.save() 
                         
            except Exception as e:
                print("codeforces profile doesn't exist",e)
        


@shared_task
def scrape_leetcode_profile():
    users = User.objects.all() # type: ignore
    for user in users:
        try:
            leetcodeid = PlatformID.objects.get(user=user).leetcodeID
            if leetcodeid:
                url = f"https://leetcode.com/{leetcodeid}/"
                leetcode_details = leetcode_profile(url)
                user_leetcode_details = LeetcodeDetails.objects.get(user=user)
                print(leetcode_details)
                user_leetcode_details.rank = leetcode_details['rank'] 
                user_leetcode_details.no_of_contest_attempted = leetcode_details['contest_attempted']
                user_leetcode_details.contest_rating = leetcode_details['contest_rating']
                user_leetcode_details.no_of_problem_solved= leetcode_details['problem_solved']
                user_leetcode_details.score = int(float(leetcode_details['contest_rating']*leetcode_details['contest_attempted']//2)*0.5+float(leetcode_details['problem_solved'])*5 )  
                user_leetcode_details.save() 
        except Exception as e:
            print("leetcode profile doesn't exist",e)
    return "done"

    

@shared_task
def scrape_spoj_profile():
    return "done"

@shared_task
def update_leaderboard():
    users = User.objects.all()
    for user in users:
        try:
            score = LeaderBoard.objects.get(user=user)
            codeforces_score = CodeforcesDetails.objects.get(user=user)
            leetcode_score = LeetcodeDetails.objects.get(user=user)
            spoj_score = SpojDetails.objects.get(user=user)
            hackerrank_score = HackerRankDetails.objects.get(user=user)
            codechef_score = CodechefDetails.objects.get(user=user) 
            score.ic_score = codechef_score.score + leetcode_score.score + codeforces_score.score + spoj_score.score + hackerrank_score.score
            score.total_problem_solved = codechef_score.no_of_problem_solved + codeforces_score.no_of_problem_solved + leetcode_score.no_of_problem_solved + spoj_score.no_of_problem_solved
            score.total_contest_attempted = codechef_score.no_of_contest_attempted +codechef_score.no_of_contest_attempted + leetcode_score.no_of_contest_attempted + spoj_score.no_of_contest_attempted
            score.save()
        except:
            print(f"{user.username} coding profile doesnot exist")
    return "done"


