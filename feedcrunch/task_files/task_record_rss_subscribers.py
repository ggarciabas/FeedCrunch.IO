#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from application.celery import app as celery

from feedcrunch.models import FeedUser
from feedcrunch.models import RSSSubsStat
from feedcrunch.models import RSSSubscriber

from datetime import datetime
from datetime import timedelta

__all__ = [
    'record_user_subscribers_stats',
    'refresh_all_rss_subscribers_count',
    'clean_unnecessary_rss_visits',
]


@celery.task(name='feedcrunch.tasks.record_user_subscribers_stats')
def record_user_subscribers_stats(username=None):

    if username is None:
        raise Exception("Username have not been provided")

    try:
        usr = FeedUser.objects.get(username=username)
    except ObjectDoesNotExist:
        raise Exception("The given username ('"+username+"') doesn't exist.")

    today           = datetime.now().date()
    yesterday       = today - timedelta(days=1)
    sub_timedelta   = settings.RSS_SUBS_LOOKUP_PERIOD
    last_lookup_day = today - timedelta(days=sub_timedelta)

    # Check if a statistic already exists for yesterday
    if not usr.rel_rss_subscribers_count.filter(date__gte=yesterday).exists():

        count = usr.rel_rss_subscribers.filter(date__gte=last_lookup_day).values("ipaddress").annotate(n=models.Count("pk")).count()

        record = RSSSubsStat.objects.create(user=username, count=count)

        if isinstance(record, dict):
            _err = "%s // Timestamp: %s // Timestamp_TZ: %s" % (
                record["error"],
                record["timestamp"].strftime("%d/%m/%y - %H:%M"),
                record["timestamp_tz"].strftime("%d/%m/%y - %H:%M")
            )
            raise Exception(_err)

    else:
        _err = "Object already exists with date: %s and it happened at date : %s." % (
            yesterday.strftime("%d/%m/%y"),
            datetime.now().strftime("%d/%m/%y - %H:%M")
        )
        raise Exception(_err)


@celery.task(name='feedcrunch.tasks.refresh_all_rss_subscribers_count')
def refresh_all_rss_subscribers_count():
    for user in FeedUser.objects.all():
        record_user_subscribers_stats.delay(username=user.username)


@celery.task(name='feedcrunch.tasks.clean_unnecessary_rss_visits')
def clean_unnecessary_rss_visits():
    today = datetime.now().date()
    date_limit = today - timedelta(days=5)

    RSSSubscriber.objects.filter(date__lte=date_limit).delete()
