import urllib2
from abc import ABCMeta, abstractmethod
import re


class BaseChat(object):
    __metaclass__ = ABCMeta
    template_name = ''
    provider_name = ''
    model = None

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.render()

    @abstractmethod
    def get_code(self):
        return self.model.identifier

    @staticmethod
    def process(chat):
        pass

    def render(self):
        try:
            return self.get_code()
        except Exception as e:
            return e.message


class ChatHitboxTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://www.hitbox.tv/embedchat/%s"></iframe>' % self.model.identifier


class ChatTwitchTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://twitch.tv/chat/embed?channel=%s&popout_chat=true"></iframe>' % self.model.identifier


class ChatCybergameTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://cybergame.tv/cgchat.htm?v=b#%s"></iframe>' % self.model.identifier


class ChatGohaTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://www.goha.tv/?iframe=true&chat=true&auth=true#!/%s"></iframe>' % self.model.identifier


class ChatGoodgameRu(BaseChat):
    def get_code(self):
        return '<iframe src="http://goodgame.ru/chat/%s/"></iframe>' % self.model.identifier


class ChatHoradricRu(BaseChat):
    def get_code(self):
        response = urllib2.urlopen('http://horadric.ru/stream/%s' % self.model.identifier)
        data = response.read()
        result = re.search('id="chat-new-window".*window.open\(\'([^\']+)\'', data)
        url = result.group(1)

        return '<iframe src="http://horadric.ru%s"></iframe>' % url


class ChatConnectcastTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://connectcast.tv/chat/embed/%s"></iframe>' % self.model.identifier


class ChatVaughnliveTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://vaughnlive.tv/popout/chat/%s"></iframe>' % self.model.identifier


class ChatVapersTv(BaseChat):
    def get_code(self):
        return '<iframe src="http://vapers.tv/popout/chat/%s"></iframe>' % self.model.identifier

class ChatSc2tvRu(BaseChat):
    def get_code(self):
        return '<iframe src="http://funstream.tv/chat/stream/%s"></iframe>' % self.model.identifier

class ChatYouTube(BaseChat):
    def get_code(self):
        return '<iframe src="https://www.youtube.com/live_chat?from_gaming=1&dark_theme=1&is_popout=1&v=%s' % self.model.identifier
