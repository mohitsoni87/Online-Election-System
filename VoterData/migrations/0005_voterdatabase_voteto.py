# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-18 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoterData', '0004_auto_20190318_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='voterdatabase',
            name='voteTo',
            field=models.CharField(default='', max_length=30),
        ),
    ]