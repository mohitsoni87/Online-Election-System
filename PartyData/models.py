# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PartyDetail(models.Model):
    Name = models.CharField(max_length=30)
    About = models.CharField(max_length=1000)
    UniqueKey = models.CharField(max_length=3, unique=True)
    Headquarters = models.CharField(max_length=30)
    Logo = models.FileField(max_length=1000, null=False)
    President = models.CharField(max_length=100)

    def __str__(self):
        return self.UniqueKey + ' - ' + self.Name

