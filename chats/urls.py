from django.conf.urls import patterns, include, url
from django.contrib import admin
import base

urlpatterns = patterns('',
                       url(r'^/ajax/delete', 'chats.ajax.delete'),
                       url(r'^/ajax/get', 'chats.ajax.get'),
                       url(r'^/ajax/new', 'chats.ajax.new'),
                       url(r'^/ajax/list', 'chats.ajax.list'),
                       url(r'^/ajax/set', 'chats.ajax.set'),
                       url(r'^', 'chats.views.index'),
)
