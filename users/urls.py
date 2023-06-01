from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index-page'),
    path("register/",views.register,name='register-page'),
    path("home/",views.home,name='home-page'),
    path("profile/",views.profile,name='profile-page'),
    path("edit_profile/",views.edit_profile,name='edit-profile'),
    path("view_profile/<str:username>/",views.view_profile,name='view-profile'),
    # path("login/",views.login,name='login')
]
