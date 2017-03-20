from django.conf.urls import patterns, include, url
from django.contrib import admin
import base

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'streamchats2.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^ajax/get_news', 'base.ajax.getNews'),
                       url(r'^ajax/set_news_read', 'base.ajax.setNewsRead'),
                       url(r'^', 'base.views.index'),
)
