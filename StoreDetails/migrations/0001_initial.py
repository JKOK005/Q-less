# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-13 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenuModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodOrderQueueModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_no', models.IntegerField(default=0)),
                ('waiting_time', models.FloatField(default=9)),
                ('food_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreDetails.FoodMenuModels')),
            ],
        ),
        migrations.CreateModel(
            name='StoreModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(default='Your store here', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='foodmenumodels',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StoreDetails.StoreModels'),
        ),
    ]