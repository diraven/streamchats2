import json
from base.classes.HttpResponseJson import HttpResponseJson
from base.models import News
from chats.forms import ChatForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core import serializers
from django.template.context import RequestContext
from django.template.loader import get_template
from chats.models import Chat, Provider
from chats.classes import provider


@login_required()
def getNews(request):
    if request.user.profile.last_news_viewed is not None:
        news = News.objects.filter(id__gt=request.user.profile.last_news_viewed.id).order_by('-id')[:3]
    else:
        news = News.objects.all().order_by('-id')[:3]

    data = {}
    for item in news:
        data[item.id] = {}
        data[item.id]['title'] = item.title
        data[item.id]['text'] = item.text
        data[item.id]['type'] = item.type
        data[item.id]['date'] = item.date.isoformat()

    return HttpResponseJson(data, True, 'News have been sent.')


def setNewsRead(request):
    item = get_object_or_404(News, id=request.GET.get('id'))
    profile = request.user.profile
    profile.last_news_viewed = item
    profile.save()
    return HttpResponseJson(None, True, 'News reading has been updated.')