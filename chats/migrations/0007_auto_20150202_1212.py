# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_auto_20150108_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='height',
            field=models.FloatField(default=300),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chat',
            name='left',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chat',
            name='top',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chat',
            name='width',
            field=models.FloatField(default=300),
            preserve_default=True,
        ),
    ]
