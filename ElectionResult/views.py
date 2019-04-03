# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as plt
from .models import ElectionResult
from django.shortcuts import render, redirect
from SectorParties.models import Sector
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import os
from Election.models import SectorDetail

from django.http import HttpResponse
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import BytesIO as StringIO
from Candidate.models import CandidateProfile



color = {'BJP': 'orange', 'CNG': 'blue', 'DMK': 'k', 'AIA': 'red'}


# def matPlotLib(data, PinCode):
#     parties = []
#     regionName = SectorDetail.objects.get(pin=PinCode).RegionName
#
#     for count, x in enumerate(data):
#
#         parties.append(x.UniqueKey)
#         plt.bar(count, x.VoterCounter, label=x.UniqueKey, color=color[x.UniqueKey])
#
#     plt.xticks(list(range(0, count + 1)), parties)
#     plt.xlabel('Election Parties')
#     plt.ylabel('Votes')
#     plt.title('Election Results for ' + regionName + ' - ' + PinCode )
#     print(True, False)
#     print(os.getcwd())
#     plt.show()
#     print(True)
#     plt.savefig(str(PinCode) + '.png')
#     print(True)
#     return plt

def electionResult(request, PinCode):
    data = Sector.objects.filter(pin=PinCode)
    # object = ElectionResult()
    # object.pin = PinCode
    # object.image = matPlotLib(data, PinCode, )
    # print(False)
    # print(object)
    # object.save()
    # print(object.pin, object.image)
    # return redirect('/')


    parties = []
    regionName = SectorDetail.objects.get(pin=PinCode).RegionName
    winner_count, winner = 0, ''
    for count, x in enumerate(data):
        if(x.VoterCounter > winner_count):
            winner_count = x.VoterCounter
            winner = x.UniqueKey

        parties.append(x.UniqueKey)
        plt.bar(count, x.VoterCounter, label=x.UniqueKey, color=color[x.UniqueKey])


    plt.xticks(list(range(0, count + 1)), parties)
    plt.xlabel('Election Parties')
    plt.ylabel('Votes')
    print(PinCode, winner)
    winningCandidate = CandidateProfile.objects.filter(pin=PinCode).filter(Party_Name=winner)[0].name
    plt.title('Election Results for ' + regionName + ' - ' + PinCode  + '\nThe winning party is ' + winner + ' with ' + str(winner_count) + ' votes.\nElected Candidate: ' + winningCandidate)


    buffer = StringIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()
    return HttpResponse(buffer.getvalue(), content_type ="image/png")
    # print(True, False)
    # print(os.getcwd())
    # plt.show()
    # print(True)
    # plt.savefig(str(PinCode) + '.png')
    # print(True)
    # return plt
# Create your views here.
