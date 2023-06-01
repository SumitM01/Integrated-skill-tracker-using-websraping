from django.db import models
from django.contrib.auth.models import User

class PlatformID(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hackerRankID = models.CharField(blank=True ,max_length=100)
    codechefID = models.CharField(blank=True ,max_length=100)
    leetcodeID = models.CharField(blank=True ,max_length=100)
    codeforcesID = models.CharField(blank=True ,max_length=100)
    spojID = models.CharField(blank=True ,max_length=100)
    
    def __str__(self):
        return f'{self.user.username} coding profile'

class HackerRankDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Badges = models.CharField(max_length=100000, blank=True)
    skill_verified = models.CharField(max_length=100000, blank=True)
    score = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return f'{self.user.username} hackerrank profile'
    

class LeetcodeDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rank=models.PositiveBigIntegerField(default=0)
    no_of_contest_attempted=models.PositiveIntegerField(default=0)
    contest_rating=models.PositiveIntegerField(default=0)
    no_of_problem_solved=models.PositiveIntegerField(default=0)
    score=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} leetcode profile'

class CodechefDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rank=models.PositiveBigIntegerField(default=0)
    no_of_contest_attempted=models.PositiveIntegerField(default=0)
    contest_rating=models.PositiveIntegerField(default=0)
    no_of_problem_solved=models.PositiveIntegerField(default=0)
    score=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} codechef profile'

class CodeforcesDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rank=models.CharField(max_length=100, null=True)
    no_of_contest_attempted=models.PositiveIntegerField(default=0)
    contest_rating=models.PositiveIntegerField(default=0)
    no_of_problem_solved=models.PositiveIntegerField(default=0)
    score=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} codeforces profile'

class SpojDetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    rank=models.PositiveBigIntegerField(default=0)
    no_of_contest_attempted=models.PositiveIntegerField(default=0)
    contest_rating=models.PositiveIntegerField(default=0)
    no_of_problem_solved=models.PositiveIntegerField(default=0)
    score=models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} spoj profile'
    
class LeaderBoard(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    total_problem_solved=models.PositiveBigIntegerField(default=0)
    total_contest_attempted=models.PositiveBigIntegerField(default=0)
    ic_score=models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ('-ic_score',)

    def __str__(self):
        return f"{self.user.username} - {self.ic_score}"


