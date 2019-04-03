# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ElectionResult(models.Model):
    pin = models.CharField(max_length=6)
    image = models.FileField(max_length=1000, null=True)
    def __str__(self):
        return str(self.pin)
