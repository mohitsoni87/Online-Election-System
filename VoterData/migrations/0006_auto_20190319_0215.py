# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-18 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoterData', '0005_voterdatabase_voteto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterdatabase',
            name='voteTo',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]
