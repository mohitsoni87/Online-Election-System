# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CandidateProfile(models.Model):
    name = models.CharField(max_length=40)
    Profile = models.FileField(max_length=1000, null=False)
    age = models.IntegerField()
    sex = models.CharField(max_length=6)
    Party_Name = models.CharField(max_length=40)
    pin = models.CharField(max_length=6)

    def __str__(self):
        return self.name + ' - ' + self.Party_Name + ' - ' + str(self.pin)

