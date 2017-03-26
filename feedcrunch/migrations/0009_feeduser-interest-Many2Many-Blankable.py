# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0008_feeduser_apikey_set_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeduser',
            name='interests',
            field=models.ManyToManyField(blank=True, related_name='users_by_interest', to='feedcrunch.Interest'),
        ),
    ]
