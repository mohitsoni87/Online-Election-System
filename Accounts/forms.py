from django import forms
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from VoterData.models import VoterDatabase
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password = password)
        if username and password:
            if not user:               # to check if the password is correct
                raise forms.ValidationError("Invalid Credentials")
            if not user.is_active:
                raise forms.ValidationError("User is not Active")
            return super(UserLoginForm, self).clean(*args, **kwargs)
        return redirect('/invalid')

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)
    mobile_number = forms.CharField(min_length=10, max_length=10)
    Voter_ID = forms.CharField(min_length=10, max_length=10)

    class Meta:
        model = User #
        fields = ['first_name', 'last_name', 'username' , 'email', 'mobile_number', 'password', 'password_confirm', 'Voter_ID']

    def clean(self, *args, **kwargs):

        check1 = self.cleaned_data.get('password')
        check2 = self.cleaned_data.get('password_confirm')
        ID = self.cleaned_data.get('Voter_ID')
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        mobile_number = self.cleaned_data.get('mobile_number')
        emailqs = User.objects.filter(email=email)
        usernameqs = User.objects.filter(username=username)
        mobile_numberqs = User.objects.filter(username=mobile_number)
        data = VoterDatabase.objects.filter(email=email)

        if (emailqs.exists()):
            raise forms.ValidationError('Email ID already exists')
        if(usernameqs.exists()):
            raise forms.ValidationError('Username already exists')
        if(mobile_numberqs.exists()):
            raise forms.ValidationError('Mobile number already exists')
        if (check1 != check2):
            raise forms.ValidationError('Password must match!')
        if(not (data)):
            raise forms.ValidationError('Your E-mail-ID is not available in our Database. Please contact the Election Office and update your Mail. Thank you.')
        if(data and data[0].VoterID != ID):
            raise forms.ValidationError('Invalid Voter-ID. Please try again.')


        return super(RegisterForm, self).clean(*args, **kwargs)