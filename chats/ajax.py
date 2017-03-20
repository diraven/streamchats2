import json
from base.classes.HttpResponseJson import HttpResponseJson
from chats.forms import ChatForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core import serializers
from django.template.context import RequestContext
from django.template.loader import get_template
from chats.models import Chat, Provider
from chats.classes import provider


@login_required
def delete(request):
    chat = get_object_or_404(Chat, id=request.GET.get('id'), user=request.user)
    chat.delete()
    return HttpResponseJson(None, True, 'Chat has been deleted!')


@login_required
def get(request):
    chat = get_object_or_404(Chat, id=request.GET.get('id'), user=request.user)
    data = {
        'id': chat.id,
        'provider_title': chat.provider.title,
        'identifier': chat.identifier,
        'code': chat.render(),
        'width': chat.width,
        'height': chat.height,
        'top': chat.top,
        'left': chat.left,
        'status': chat.status,
    }
    return HttpResponseJson(data, True, 'Chat data sent.')


@login_required
def set(request):
    chat = get_object_or_404(Chat, id=request.GET.get('id'), user=request.user)
    chat.top = request.GET.get('top') or chat.top
    chat.left = request.GET.get('left') or chat.left
    chat.width = request.GET.get('width') or chat.width
    chat.height = request.GET.get('height') or chat.height
    if (request.GET.get('status') in [
        'initialized',
        'normalized',
        'maximized',
        'minimized',
        'smallified',
        'smallifiedMax',
    ]):
        chat.status = request.GET.get('status') or chat.status
    chat.save()
    return HttpResponseJson(None, True, 'Changes saved.')


@login_required
def list(request):
    data = []
    for chat in Chat.objects.all().filter(user=request.user):
        data.append({
            'id': chat.id,
        })

    return HttpResponseJson(data, True, 'Chat list sent.')


@login_required
def new(request):
    t = get_template('chats/forms/new_chat.html')
    if request.method == "GET":
        f = ChatForm()
        c = RequestContext(request, {'form': f})
        return HttpResponseJson(t.render(c), True, 'Form data sent.')

    if request.method == "POST":
        f = ChatForm(request.POST)
        c = RequestContext(request, {'form': f})
        if f.is_valid():
            instance = f.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseJson(instance.id, True, 'Chat saved.')
        return HttpResponseJson(t.render(c), False, 'Validation errors.')
