# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-18 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VoterData', '0006_auto_20190319_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voterdatabase',
            name='voteTo',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
