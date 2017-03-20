# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_auto_20150104_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='status',
            field=models.CharField(default=b'normalized', max_length=32, choices=[(0, b'initialized'), (0, b'normalized'), (0, b'maximized'), (0, b'minimized'), (0, b'smallified'), (0, b'smallifiedMax')]),
            preserve_default=True,
        ),
    ]
