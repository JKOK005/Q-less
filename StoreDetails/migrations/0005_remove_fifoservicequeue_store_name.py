# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 12:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreDetails', '0004_auto_20170513_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fifoservicequeue',
            name='store_name',
        ),
    ]
