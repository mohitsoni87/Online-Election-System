# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import PartyDetail
from django.shortcuts import render
def detailView(request, UniqueKey):
    partyInfo = PartyDetail.objects.get(UniqueKey=UniqueKey)
    return render(request, 'PartyData/PartyDetail.html', {'partyInfo': partyInfo})


