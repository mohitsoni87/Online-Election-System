from django.shortcuts import render
from VoterData.models import VoterDatabase
from datetime import datetime
from Election.models import SectorDetail
htmlFile = "OnlineElectionSystem/homepage.html"
electionStatus = 0
electionResult = 0
def homepage(request):
    anonymous = request.user.is_anonymous
    global electionStatus
    if(not anonymous):
        data = VoterDatabase.objects.all().get(email = request.user.email)
        electionData = SectorDetail.objects.get(pin = data.pin)


        #One day election
        if(datetime.now().date() == electionData.Startdate.date() and electionData.Startdate.date() == electionData.Enddate.date()):
            if(datetime.now().time() >= electionData.Startdate.time() and datetime.now().time() <= electionData.Enddate.time()):

                electionStatus = 1
            else:
                electionStatus = 0
        #Day 1
        elif(datetime.now().date() == electionData.Startdate.date()):
            if(datetime.now().time() >= electionData.Startdate.time()):
                electionStatus = 1
            else:
                electionStatus = 0
        #Day N
        elif(datetime.now().date() == electionData.Enddate.date()):
            if(datetime.now().time() <= electionData.Enddate.time()):
                electionStatus = 1
            else:
                electionStatus = 0
        elif(datetime.now().date() > electionData.Startdate.date() and datetime.now().date() < electionData.Enddate.date()):
            electionStatus = 1
        else:
            electionStatus = 0

        #checking for election Result
        if(electionStatus):
            if(datetime.now().date() == electionData.Resultdate.date() and datetime.now().time() >= electionData.Resultdate.time()):
                electionResult = 1
            elif(datetime.now().date() > electionData.Resultdate.date()):
                electionResult = 1
            else:
                electionResult = 0
        else:
            electionResult = 0

        return render(request, htmlFile, {'data': data, 'dateTimeObject': datetime.now(), 'electionData': electionData, 'electionStatus': electionStatus, 'electionResult': electionResult})
    return render(request, htmlFile)
