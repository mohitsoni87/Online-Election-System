# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-21 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=6)),
                ('image', models.FileField(max_length=1000, null=True, upload_to=b'')),
            ],
        ),
    ]
