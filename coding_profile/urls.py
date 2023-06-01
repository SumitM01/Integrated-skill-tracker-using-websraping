from django.urls import path
from . import views

urlpatterns = [
    path('stat/',views.stat,name='stat-page'),
    path('leaderboard/',views.leaderboard,name='leaderboard-page')
]