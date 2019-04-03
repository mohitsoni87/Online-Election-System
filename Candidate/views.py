# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import CandidateProfile
from django.shortcuts import render

def profile(request, PinCode, UniqueKey):
    print(PinCode, UniqueKey)#
    object = CandidateProfile.objects.filter(pin=PinCode).filter(Party_Name=UniqueKey)[0]

    print(object, True)
    return render(request, 'Candidate/Profile.html', {'object': object})

