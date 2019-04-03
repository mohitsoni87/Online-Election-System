
from __future__ import unicode_literals
from django.db import models


class SectorDetail(models.Model):
    pin = models.CharField(max_length=6)
    RegionName = models.CharField(max_length=40, null=False)
    Startdate = models.DateTimeField(blank=True)
    Enddate = models.DateTimeField(blank=True)
    Resultdate = models.DateTimeField(blank=True,)
    def __str__(self):
        return self.pin + ' - ' + self.RegionName + ' - ' + str(self.Startdate.time()) + ' - ' + str(self.Startdate.date()) + ' - ' + str(self.Enddate.time()) + ' - ' + str(self.Enddate.date())