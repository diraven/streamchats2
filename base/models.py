from django.contrib.auth.models import User
from django.db import models
import datetime
from tinymce.models import HTMLField
from streamchats2 import settings


class News(models.Model):
    date = models.DateField(default=datetime.date.today, null=False)
    title = models.CharField(max_length=128, null=False)
    text = HTMLField(null=False)
    type = models.CharField(max_length=32, choices=(
        ('alert', 'alert'),
        ('success', 'success'),
        ('error', 'error'),
        ('warning', 'warning'),
        ('information', 'information'),
        ('confirm', 'confirm'),
    ), default='information', null=False)

    def __unicode__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User)
    last_news_viewed = models.ForeignKey(News, null=True)


User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])