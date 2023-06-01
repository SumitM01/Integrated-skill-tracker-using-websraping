from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import PlatformID,HackerRankDetails,CodechefDetails,CodeforcesDetails,LeetcodeDetails,SpojDetails,LeaderBoard

@receiver(post_save,sender=User)
def create_coding_profile(sender,instance,created,**kwargs):
    if created:
        PlatformID.objects.create(user=instance)
        HackerRankDetails.objects.create(user=instance)
        CodechefDetails.objects.create(user=instance)
        CodeforcesDetails.objects.create(user=instance)
        LeetcodeDetails.objects.create(user=instance)
        SpojDetails.objects.create(user=instance)
        LeaderBoard.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_coding_profile(sender,instance,**kwargs):
    instance.platformid.save()
    instance.hackerrankdetails.save()
    instance.codechefdetails.save()
    instance.codeforcesdetails.save()
    instance.leetcodedetails.save()
    instance.spojdetails.save()
    instance.leaderboard.save()
