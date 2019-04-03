# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout, get_user_model
from Accounts.forms import UserLoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.contrib import auth
from django import forms
from OnlineElectionSystem import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from VoterData.models import VoterDatabase
import random
import requests
import json

URL = 'http://www.way2sms.com/api/v1/sendCampaign'


#SEND OTP

def sendOTP(number, fullName):
# get request

    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage, token, fullName):

        for i in range(5):
            token += str(random.randrange(0, 9))
        message = "Hello, " + fullName + ".\nYour OTP is " + token + ".\n"
        req_params = {
          'apikey':'R3FJIS9POTNPTVRI45IDLEYL4NY2T9M8',
          'secret':'3U0XBJXPI4BH8EBC',
          'usetype':'stage',
          'phone': str(number),
          'message':message,
          'senderid':'Mohit Soni'
          }
        return requests.post(reqUrl, req_params),token

    # get response
    response, token = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text', "", fullName)
    # print response if you want
    return (response.text), token



def login_view(request):
    form = UserLoginForm(request.POST or None)
    return  render(request, "Accounts/Login.html", {'form': form, 'title': 'Login'})

def auth_view(request):

    form = UserLoginForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username = username, password=password)
        if not user:
            raise forms.ValidationError('Invalid credentials.')
        else:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
    else:
        return render(request, 'Accounts/InvalidCredentials.html')
            
def register_view(request):

    form = RegisterForm(request.POST or None)


    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        number = form.cleaned_data.get('mobile_number')
        fullName =  form.cleaned_data.get('first_name') + " " + form.cleaned_data.get('last_name')
        text, token = sendOTP(number, fullName)
        user.otp = token
        print(token)
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return render(request, "Accounts/OTP.html", {'token': token})


    context = {'form': form, 'title': 'Register '}
    return  render(request, 'Accounts/form.html', context)



def RegisterUser(request):
    token = request.GET.get('q').strip()
    link = '192.168.43.227:8000'
    #link = "127.0.0.1:8000"
    CheckUser = request.user
    print(CheckUser.otp)
    if(CheckUser.otp == token):
        to_send = [str(CheckUser.email)]
        link = "http://" + link + "/account_verification/" + CheckUser.username + "/" + CheckUser.token
        message = "Hello, " + str(CheckUser.username) + "\nPlease click on the following link to verify your account " + str(link)
        # send_mail(subject, message, from, to, fail_silently=True)
        send_mail('E-Mail Verification.', message, settings.EMAIL_HOST_USER, to_send, fail_silently=False)
        return redirect('/')
    getuser = User.objects.get(username = CheckUser.username)
    getuser.delete()
    return render(request, 'Accounts/FailedOTP.html')


def AccountVerification(request, username, token):
    object = User.objects.all().get(username=username)

    if(object.acc_activation):
        return render(request, 'Accounts/Already_Verified.html', {'object': object})

    #Mail TOKEN verification

    if(token == object.token):
        object.acc_activation = True
        object.save()
        object = User.objects.all().get(username=username)
        return render(request, 'Accounts/Verified.html', {'object': object})
    else:
        return render(request, 'Accounts/Unsuccessfull.html')



def ProfileView(request):
    object = VoterDatabase.objects.all().get(email=request.user.email)
    return render(request, 'Accounts/Profile.html', {'object': object})

def logout_view(request):
    logout(request)
    return  redirect('/')