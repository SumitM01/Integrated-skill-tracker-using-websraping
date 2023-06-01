from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .form import UserRegisterForm, EditProfileForm,EditPlatformIDForm,LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from verify_email.email_handler import send_verification_email
from coding_profile.models import LeaderBoard
from contest.models import Contest
from .models import Profile
from courses.models import UserCodingQuestion,CodingQuestion
    

def index(request):
    return render(request,'index.html')

@login_required
def home(request): 
    leaderboard = LeaderBoard.objects.all()
    contests = Contest.objects.filter(status='ongoing')
    for contest in contests:
        contest.time = contest.time.strftime('%H:%M:%S')
    questions =  CodingQuestion.objects.filter()
    question = questions.count()
    user_questions = UserCodingQuestion.objects
    solved = user_questions.filter(user=request.user,is_done=True).count()
    return render(request,'home.html',{"leaderboard":leaderboard, "contest":contests, "questions":questions, 
                                       "userquestions":user_questions, "question":question, "solved":solved})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request)
                return redirect('home-page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request, form)
            username=form.cleaned_data.get('username')
            messages.info(request,f'A mail is send to your registered mail id for verification')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        form = EditPlatformIDForm(request.POST,instance=request.user.platformid)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your PlatformID has been updated...')
            return redirect('profile-page')
    else:
        form=EditPlatformIDForm(instance=request.user.platformid)
    user_profile = Profile.objects.get(user=request.user)
    user_skills = user_profile.skills.all()
    return render(request,'profile.html',{'form':form,'user_skills':user_skills})

@login_required
def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your profile has been updated...')
            return redirect('profile-page')
    else:
        form=EditProfileForm(instance=request.user.profile)
    return render(request,'edit_profile.html',{'form':form})

@login_required
def view_profile(request, username):
    view_user= User.objects.get(username=username)
    user_profile = Profile.objects.get(user=view_user)
    user_skills = user_profile.skills.all()
    return render(request, 'view_profile.html', {'view_user':view_user,'user_skills':user_skills})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

