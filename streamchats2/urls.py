from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.template import base

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'streamchats2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^tinymce', include('tinymce.urls')),
    url(r'^chats', include('chats.urls')),
    url(r'^', include('base.urls')),
)
