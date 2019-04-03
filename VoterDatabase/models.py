# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class VoterDatabase(models.Model):
    first_name = models.CharField(max_length = 100, null=False)
    last_name = models.CharField(max_length = 100, null=False)
    email = models.EmailField()
    VoterID = models.CharField(max_length = 10, null=False)
    Age = models.IntegerField(max_length=10)
    Sex = models.CharField(max_length=5)
    pin = models.IntegerField(max_length=6)
    mobile_number = models.CharField(max_length=10, default="", null=False)
    #pin = models.CharField(max_length=6, null=False)
    regionOfVoting = models.CharField(max_length=30, null=False)
    def __str__(self):
        return self.email + ' - ' + self.VoterID
# Create your models here.


