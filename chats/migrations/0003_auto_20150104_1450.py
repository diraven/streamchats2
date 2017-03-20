# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20150104_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='x',
            new_name='left',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='y',
            new_name='top',
        ),
    ]
