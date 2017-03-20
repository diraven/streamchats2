from django.contrib.auth.models import User
from django.db import models
from chats.classes import provider

# class

class Provider(models.Model):
    title = models.CharField(max_length=64, null=False)
    class_name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.title

class Chat(models.Model):
    user = models.ForeignKey(User)
    provider = models.ForeignKey(Provider)
    identifier = models.CharField(max_length=64, null=False)
    top = models.FloatField(null=False, default=0)
    left = models.FloatField(null=False, default=0)
    width = models.FloatField(null=False, default=300)
    height = models.FloatField(null=False, default=300)
    status = models.CharField(max_length=32, choices=(
        ('initialized', 'initialized'),
        ('normalized', 'normalized'),
        ('maximized', 'maximized'),
        ('minimized', 'minimized'),
        ('smallified', 'smallified'),
        ('smallifiedMax', 'smallifiedMax'),
    ), default='normalized', null=False)

    def save(self, *args, **kwargs):
        klass = getattr(provider, self.provider.class_name)
        klass.process(self)
        super(Chat, self).save(*args, **kwargs)

    def render(self):
        service_chat = getattr(provider, self.provider.class_name)(self)
        return service_chat.render()
