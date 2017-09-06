#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import include, url
import django.contrib.auth.views
from django.views.decorators.csrf import csrf_exempt

#from .admin import admin_site
from .views import *
from rest_framework.authtoken import views

urlpatterns = [

    # ====================== Public API Routes ====================== #

    url(r'^public/post/validate/username/$', Username_Validation.as_view(), name='validate_username'),
    url(r'^public/post/validate/rssfeed/$', rssfeed_Validation.as_view(), name='validate_username'),

    # ====================== Authentication Required API Routes ====================== #
    # Login/Logout Route
    url(r'^get_auth_token/$', views.obtain_auth_token, name='Obtain_Auth_Token'),
    url(r'^logout/$', django.contrib.auth.views.logout, {'next_page': '/login',}, name='logout'),

    # User Routes
    url(r'^authenticated/get/user/publications_stats/$', User_Stats_Publications.as_view(), name='publications_stats'),
    url(r'^authenticated/get/user/subscribers_stats/$', User_Stats_Subscribers.as_view(), name='subscribers_stats'),
    url(r'^authenticated/modify/user/social-networks/slack/$', Modify_Slack_Preferences.as_view(), name='modify_slack_preferences'),
    url(r'^authenticated/modify/user/social-networks/$', Modify_Social_Networks.as_view(), name='modify_social_networks'),
    url(r'^authenticated/modify/user/personal-info/$', Modify_Personal_info.as_view(), name='Modify_Personal_info'),
    url(r'^authenticated/modify/user/password/$', Modify_Password.as_view(), name='Modify_Password'),
    url(r'^authenticated/modify/user/preferences/$', User_Preferences.as_view(), name='modify_preferences'),

    # OAUTH Social Networks Routes
    url(r'^authenticated/get/user/social-networks/(?P<social_network>\w+)/status/$', User_Social_Network_Status.as_view(), name='User_Social_Network_Status'),
    url(r'^authenticated/delete/user/social-networks/(?P<social_network>\w+)/$', UnLink_User_Social_Network.as_view(), name='UnLink_Social_Network'),

    # Tag Routes
    url(r'^authenticated/get/tags/$', Tags.as_view(), name='tags_as_json'),

    # RSSArticle Routes
    url(r'^authenticated/mark_as_read/rssarticle/(?P<RSSArticle_AssocID>\d+)/$', RSSArticle_Assoc_View.as_view(), name='Mark_As_Read_RSSArticle_Assoc'),
    url(r'^authenticated/mark_list_as_read/rssarticle/$', RSSArticle_Assoc_View.as_view(), name='Mark_List_As_Read_RSSArticle_Assoc'),

    # RSSFeed Subscribtions Routes
    url(r'^authenticated/post/rssfeed_subscribtion/$', RSSFeed_View.as_view(), name='create_RSSFeed'),
    url(r'^authenticated/import/opml_file/$', OPML_Management.as_view(), name='Import OPML'),
    url(r'^authenticated/export/opml_file/$', OPML_Management.as_view(), name='Export OPML'),

    # RSSFeed_Sub Subscribtions Routes
    url(r'^authenticated/delete/rssfeed_subscribtion/(?P<RSSFeed_SubID>\d+)/$', RSSFeed_Sub_View.as_view(), name='delete_RSSFeed'),
    url(r'^authenticated/modify/rssfeed_subscribtion/(?P<RSSFeed_SubID>\d+)/$', RSSFeed_Sub_View.as_view(), name='modify_RSSFeed'),

    # Article Routes
    url(r'^authenticated/get/article/exists/(?P<APIKey>[^/]+)/$', Article_Exists.as_view(), name='Get_Article_Exists'),
    url(r'^authenticated/get/article/exists/$', Article_Exists.as_view(), name='Get_Article_Exists'),
    url(r'^authenticated/post/article/(?P<APIKey>[^/]+)/$', Article.as_view(), name='post_article_with_APIKey'),
    url(r'^authenticated/post/article/$', Article.as_view(), name='post_article'),
    url(r'^authenticated/modify/article/(?P<postID>\d+)/$', Article.as_view(), name='modify_article'),
    url(r'^authenticated/delete/article/(?P<postID>\d+)/$', Article.as_view(), name='delete_article'),

    # ====================== Private API Routes - API KEY REQUIRED ====================== #

    # Article Routes
    url(r'^private/get/article/(?P<postID>\d+)/$', Article.as_view(), name='get_article'),
]
