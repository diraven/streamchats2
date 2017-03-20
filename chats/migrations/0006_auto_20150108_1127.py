# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_auto_20150106_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(default=b'normalized', max_length=32, choices=[(b'initialized', b'initialized'), (b'normalized', b'normalized'), (b'maximized', b'maximized'), (b'minimized', b'minimized'), (b'smallified', b'smallified'), (b'smallifiedMax', b'smallifiedMax')]),
            preserve_default=True,
        ),
    ]
