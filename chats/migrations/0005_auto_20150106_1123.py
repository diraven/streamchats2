# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_chat_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(default=b'normalized', max_length=32, choices=[(0, b'initialized'), (1, b'normalized'), (2, b'maximized'), (3, b'minimized'), (4, b'smallified'), (5, b'smallifiedMax')]),
            preserve_default=True,
        ),
    ]
