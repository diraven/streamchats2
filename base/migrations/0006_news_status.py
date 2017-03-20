# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20150107_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='status',
            field=models.CharField(default=b'information', max_length=32, choices=[(0, b'alert'), (1, b'success'), (2, b'error'), (3, b'warning'), (4, b'information'), (5, b'confirm')]),
            preserve_default=True,
        ),
    ]
