# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UpdateSeats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableOccupancyTimeModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('no_of_occupied_seats', models.IntegerField(default=0)),
            ],
        ),
    ]
