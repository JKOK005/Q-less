# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StoreDetails', '0003_auto_20170513_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='fifoservicequeue',
            name='store_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StoreDetails.StoreModels'),
        ),
        migrations.AlterField(
            model_name='fifoservicequeue',
            name='food_menu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='StoreDetails.FoodMenuModels'),
        ),
    ]
