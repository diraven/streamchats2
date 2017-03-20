# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='height',
            field=models.IntegerField(default=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chat',
            name='width',
            field=models.IntegerField(default=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chat',
            name='x',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chat',
            name='y',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
