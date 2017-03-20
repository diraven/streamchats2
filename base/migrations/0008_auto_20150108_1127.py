# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20150107_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='type',
            field=models.CharField(default=b'information', max_length=32, choices=[(b'alert', b'alert'), (b'success', b'success'), (b'error', b'error'), (b'warning', b'warning'), (b'information', b'information'), (b'confirm', b'confirm')]),
            preserve_default=True,
        ),
    ]
