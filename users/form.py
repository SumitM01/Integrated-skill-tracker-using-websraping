from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from coding_profile.models import PlatformID


class LoginForm(forms.Form):
    username = forms.CharField(
        label="",  
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label="", 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
        validators=[]
    )
    email = forms.EmailField( 
        label="",
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        validators=[]
    )
    password1 = forms.CharField( 
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        validators=[]
    )
    password2 = forms.CharField( 
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}), 
        validators=[]
    )

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ['institute','yop','course','fullname','gender','about','city','skills','state','image']
        
    
class EditPlatformIDForm(forms.ModelForm):

    class Meta:
        model = PlatformID
        fields = ['hackerRankID','codechefID','leetcodeID','codeforcesID','spojID']
        
    