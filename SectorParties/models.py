# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Sector(models.Model):
    pin = models.CharField(max_length=6)
    Party_Name = models.CharField(max_length=40)
    CandidateName = models.CharField(max_length=40, default='')
    RegionName = models.CharField(max_length=40, null=False, default='')
    StateName = models.CharField(max_length=40, null=False, default='')
    UniqueKey = models.CharField(max_length=3)
    VoterCounter = models.IntegerField(default=0)
    Logo = models.FileField(max_length=1000, null=False, default='')


    def __str__(self):
        return self.pin + ' - ' + self.RegionName + ' - ' + self.UniqueKey + ' - ' + str(self.VoterCounter)

# Create your models here.
