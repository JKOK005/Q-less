# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UpdateSeats', '0002_tableoccupancytimemodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableoccupancytimemodels',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
