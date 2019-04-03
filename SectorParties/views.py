# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Sector
from django.shortcuts import render
from PartyData.models import PartyDetail
from Election.models import SectorDetail
from datetime import datetime
electionResult = 0
def makePartyObject(sector_object):
    party_object = {}
    for _ in sector_object:
        temp = PartyDetail.objects.get(UniqueKey=_.UniqueKey).Logo
        party_object[_.UniqueKey] = temp
    return party_object

def results(request):

    query = request.GET.get('q').strip()
    if(query == ""):
        return redirect('/')

    # PARTY INFORMATION

    sector_object = Sector.objects.filter(Party_Name=query.upper())
    print(sector_object)
    if (sector_object):
            status = 'noloop'
            party_object = PartyDetail.objects.filter(UniqueKey=sector_object[0].UniqueKey)
            print(party_object[0].Name)
            return render(request, 'SectorParties/SearchBar.html',
                          {'sector_object': sector_object, 'query': query, 'party_object': party_object,
                           'status': status})

    # PARTY INFORMATION
    sector_object = Sector.objects.filter(UniqueKey=query.upper())
    if (sector_object):
            status = 'noloop'
            party_object = PartyDetail.objects.filter(UniqueKey=sector_object[0].UniqueKey)
            return render(request, 'SectorParties/SearchBar.html',
                          {'sector_object': sector_object, 'query': query, 'party_object': party_object,
                           'status': status})



#PIN AREA WISE PARTICIPATING PARTIES

    sector_object = Sector.objects.filter(pin = query)

    if(sector_object):

        #Election Result
        electionData = SectorDetail.objects.get(pin=query)
        if (datetime.now().date() == electionData.Resultdate.date() and datetime.now().time() >= electionData.Resultdate.time()):
            electionResult = 1
        elif (datetime.now().date() > electionData.Resultdate.date()):
            electionResult = 1
        else:
            electionResult = 0

        status = 'loop'
        party_object = makePartyObject(sector_object)
        return render(request, 'SectorParties/SearchBar.html',
                      {'sector_object': sector_object, 'query': query, 'party_object': party_object, 'status': status, 'electionResult': electionResult})






#PARTIES STANDING IN A PARTICULAR REGION

    sector_object = Sector.objects.filter(RegionName = query.upper())
    if(sector_object):
        status = 'loop'
        party_object = makePartyObject(sector_object)
        return render(request, 'SectorParties/SearchBar.html',
                      {'sector_object': sector_object, 'query': query, 'party_object': party_object, 'status': status})


#StateWise Participating Parites

    sector_object = Sector.objects.filter(StateName = query.upper())
    if(sector_object):
        status = 'loop'
        party_object = makePartyObject(sector_object)
        return render(request, 'SectorParties/SearchBar.html',
                      {'sector_object': sector_object, 'query': query, 'party_object': party_object, 'status': status})


    return render(request, 'SectorParties/NoResult.html')


