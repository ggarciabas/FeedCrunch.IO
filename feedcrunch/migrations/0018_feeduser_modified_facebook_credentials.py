# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcrunch', '0017_feeduser_pref_newsletter_subscribtion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feeduser',
            old_name='facebook_token',
            new_name='facebook_access_token',
        ),
        migrations.RemoveField(
            model_name='feeduser',
            name='facebook_token_secret',
        ),
        migrations.AddField(
            model_name='feeduser',
            name='facebook_token_expire_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
