# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from SectorParties.models import Sector
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from SectorParties.models import Sector
from VoterData.models import VoterDatabase
from .models import SectorDetail
#from Candidate
def ConductElection(request, PinCode):
    parties = Sector.objects.filter(pin=PinCode)
    return render(request, 'Election/Party.html', {'data': parties})


def VoteSubmit(request, UniqueKey):
    user = request.user
    user = User.objects.get(username=user)
    voterdata = VoterDatabase.objects.get(email=user.email)
    user.vote = 1
    party = Sector.objects.filter(pin=voterdata.pin).filter(UniqueKey=UniqueKey)[0]
    party.VoterCounter += 1
    party.save()
    user.save()
    return redirect('/')

# Create your views here.
